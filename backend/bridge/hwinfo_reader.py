"""
HwinfoReader — reads the sensor tree out of HWiNFO's shared-memory block.

HWiNFO publishes every sensor it knows about to a named shared section
(``Global\\HWiNFO_SENS_SM2``) once "Shared Memory Support" is ticked in
Settings > Main Settings. The block holds two tables: a *sensor* table (the
hardware sources — CPU, GPU, drives, motherboard) and a *reading* table (the
individual values, each pointing back at its sensor by row index).

Three details make this fiddlier than a plain struct unpack, and all three are
handled explicitly:

* **The section must be opened, never created.** See ``shared_memory.py`` — the
  obvious ``mmap`` route creates the section when it is absent, which turns "is
  HWiNFO running?" into "here are some zeroes".

* **Struct layout varies.** The published C structs use natural alignment, so
  ``poll_time`` and the four ``double`` fields sit on 8-byte boundaries with
  padding in front of them. The header is parsed by trying the aligned form
  first and validating the result, and the reading layout is chosen from the
  element size the header itself reports. Rows are always walked using that
  element size, so a future HWiNFO that appends fields still reads correctly.

* **Row indices are not stable.** HWiNFO renumbers rows whenever sensors come
  and go — a drive spinning up, a GPU waking from idle, a fan controller
  appearing. Channels are keyed by the ``(sensor id, sensor instance, reading
  id)`` triple, which is stable across those changes, and the row map is
  rebuilt whenever a lookup no longer agrees.
"""
import logging
import platform
import socket
import struct
import time
from dataclasses import dataclass

from bridge.sample_value import SampleValue
from bridge.shared_memory import SharedMemoryError, SharedMemoryView
from bridge.telemetry_list import TelemetryList

logger = logging.getLogger(__name__)

SHARED_MEM_NAME = "Global\\HWiNFO_SENS_SM2"
SIGNATURE = 0x53695748  # "HWiS" as a little-endian DWORD

# Header: signature, version, revision, poll_time, then the two table descriptors.
# MSVC aligns the 8-byte poll_time, leaving 4 bytes of padding after dwRevision.
_HEADER_ALIGNED = "<III4xqIIIIII"  # 48 bytes
_HEADER_PACKED = "<IIIqIIIIII"     # 44 bytes — fallback only

# Sensor rows contain no 8-byte members, so both layouts agree at 264 bytes.
_SENSOR_FMT = "<II128s128s"

# Reading rows: under natural alignment 4 bytes of padding land before the
# doubles, giving 320 bytes against the packed form's 316.
_READING_ALIGNED = "<III128s128s16s4xdddd"  # 320 bytes
_READING_PACKED = "<III128s128s16sdddd"     # 316 bytes

READING_TYPE_NONE = 0
READING_TYPE_TEMP = 1
READING_TYPE_VOLT = 2
READING_TYPE_FAN = 3
READING_TYPE_CURRENT = 4
READING_TYPE_POWER = 5
READING_TYPE_CLOCK = 6
READING_TYPE_USAGE = 7
READING_TYPE_OTHER = 8

READING_TYPE_NAMES = {
    READING_TYPE_NONE: "None",
    READING_TYPE_TEMP: "Temperature",
    READING_TYPE_VOLT: "Voltage",
    READING_TYPE_FAN: "Fan",
    READING_TYPE_CURRENT: "Current",
    READING_TYPE_POWER: "Power",
    READING_TYPE_CLOCK: "Clock",
    READING_TYPE_USAGE: "Usage",
    READING_TYPE_OTHER: "Other",
}

# Guard rails for header validation — a plausible machine is nowhere near these.
_MAX_SENSORS = 4096
_MAX_READINGS = 65536

_SHARED_MEMORY_HINT = (
    "Could not read HWiNFO's shared memory. Check that HWiNFO is running and "
    "that Settings > Main Settings > 'Shared Memory Support' is enabled. On the "
    "free version that setting switches itself off again after 12 hours."
)


class HwinfoUnavailable(RuntimeError):
    """Raised when the shared-memory block is missing or unreadable."""


class _LayoutChanged(RuntimeError):
    """Internal: cached row indices no longer match, a re-scan is needed."""


@dataclass(frozen=True)
class SharedMemHeader:
    version: int
    revision: int
    poll_time: int
    sensor_offset: int
    sensor_element_size: int
    sensor_count: int
    reading_offset: int
    reading_element_size: int
    reading_count: int

    @property
    def total_size(self) -> int:
        return self.reading_offset + self.reading_element_size * self.reading_count


@dataclass(frozen=True)
class HwinfoReading:
    """One value from HWiNFO's reading table, with its owning sensor resolved."""

    sensor_id: int
    sensor_instance: int
    reading_id: int
    sensor_name: str
    label: str
    unit: str
    reading_type: int
    value: float
    value_min: float
    value_max: float
    value_avg: float

    @property
    def triple(self) -> tuple[int, int, int]:
        return (self.sensor_id, self.sensor_instance, self.reading_id)

    @property
    def type_name(self) -> str:
        return READING_TYPE_NAMES.get(self.reading_type, "Other")


def _cstr(raw: bytes) -> str:
    """Decode a fixed-width, NUL-terminated ANSI field from the block."""
    return raw.split(b"\0", 1)[0].decode("latin-1", "replace").strip()


class HwinfoReader:
    def __init__(self, shared_mem_name: str = SHARED_MEM_NAME) -> None:
        self._shared_mem_name = shared_mem_name
        self._view: SharedMemoryView | None = None
        self._connected = False
        self._header: SharedMemHeader | None = None
        self._reading_fmt: str = _READING_ALIGNED
        self._last_error: str | None = None
        # metric_key -> (sensor_id, sensor_instance, reading_id), set by bind_channels()
        self._channel_triples: dict[str, tuple[int, int, int]] = {}
        # Cached from the last full enumeration, used by the fast sampling path
        self._row_by_triple: dict[tuple[int, int, int], int] = {}
        self._sensor_ids: list[tuple[int, int]] = []
        self._value_offset: int = 0

    # --- lifecycle ------------------------------------------------------

    def connect(self) -> bool:
        if self._connected:
            return True
        try:
            self._open()
        except HwinfoUnavailable as e:
            self._last_error = str(e)
            logger.warning("HWiNFO shared memory unavailable: %s", e)
            return False
        logger.info(
            "Connected to HWiNFO shared memory (v%d rev%d, %d sensors, %d readings)",
            self._header.version,
            self._header.revision,
            self._header.sensor_count,
            self._header.reading_count,
        )
        return True

    def disconnect(self) -> None:
        self._close()
        logger.info("Disconnected from HWiNFO shared memory")

    def is_connected(self) -> bool:
        return self._connected

    @property
    def last_error(self) -> str | None:
        return self._last_error

    @property
    def header(self) -> SharedMemHeader | None:
        return self._header

    def poll_age_seconds(self) -> float | None:
        """Seconds since HWiNFO last refreshed the block, or None if unknown.

        A steadily climbing age means HWiNFO has stopped publishing — most often
        the free build's 12-hour shared-memory timeout, or the app being closed.
        """
        if not self._connected:
            return None
        try:
            header = self._read_header()
        except HwinfoUnavailable:
            return None
        if header.poll_time <= 0:
            return None
        return max(0.0, time.time() - header.poll_time)

    def _open(self) -> None:
        try:
            view = SharedMemoryView(self._shared_mem_name)
        except SharedMemoryError as e:
            raise HwinfoUnavailable(f"{_SHARED_MEMORY_HINT} ({e})") from e

        self._view = view
        try:
            self._header = self._read_header()
        except HwinfoUnavailable:
            self._close()
            raise

        size = self._header.reading_element_size
        if size >= struct.calcsize(_READING_ALIGNED):
            self._reading_fmt = _READING_ALIGNED
        elif size >= struct.calcsize(_READING_PACKED):
            self._reading_fmt = _READING_PACKED
        else:
            self._close()
            raise HwinfoUnavailable(
                f"Reading element size {size} is smaller than any known layout"
            )
        # Byte offset of the Value double inside a reading row, for the fast path.
        self._value_offset = struct.calcsize(self._reading_fmt) - 4 * 8

        self._connected = True
        self._last_error = None

    def _close(self) -> None:
        if self._view is not None:
            try:
                self._view.close()
            except Exception as e:
                logger.debug("Error closing shared memory: %s", e)
        self._view = None
        self._connected = False
        self._header = None
        self._row_by_triple = {}
        self._sensor_ids = []

    def _reopen(self) -> bool:
        """Drop the current view and try a fresh one (HWiNFO restarted)."""
        self._close()
        try:
            self._open()
            logger.info("Reconnected to HWiNFO shared memory")
            return True
        except HwinfoUnavailable as e:
            self._last_error = str(e)
            return False

    # --- parsing --------------------------------------------------------

    def _read(self, offset: int, size: int) -> bytes:
        view = self._view
        if view is None:
            raise HwinfoUnavailable("Shared memory is not open")
        try:
            return view.read(offset, size)
        except SharedMemoryError as e:
            raise HwinfoUnavailable(str(e)) from e

    def _read_header(self) -> SharedMemHeader:
        view = self._view
        if view is None:
            raise HwinfoUnavailable("Shared memory is not open")

        for fmt in (_HEADER_ALIGNED, _HEADER_PACKED):
            size = struct.calcsize(fmt)
            if view.size < size:
                continue
            fields = struct.unpack(fmt, self._read(0, size))
            header = SharedMemHeader(
                version=fields[1],
                revision=fields[2],
                poll_time=fields[3],
                sensor_offset=fields[4],
                sensor_element_size=fields[5],
                sensor_count=fields[6],
                reading_offset=fields[7],
                reading_element_size=fields[8],
                reading_count=fields[9],
            )
            if fields[0] == SIGNATURE and self._header_is_sane(header, size, view.size):
                return header

        raise HwinfoUnavailable(
            "Shared memory block did not match any known HWiNFO layout "
            "(bad signature or implausible table descriptors)"
        )

    @staticmethod
    def _header_is_sane(header: SharedMemHeader, header_size: int, view_size: int) -> bool:
        if not (0 < header.sensor_element_size <= 4096):
            return False
        if not (0 < header.reading_element_size <= 4096):
            return False
        if not (0 <= header.sensor_count <= _MAX_SENSORS):
            return False
        if not (0 <= header.reading_count <= _MAX_READINGS):
            return False
        if header.sensor_offset < header_size or header.reading_offset < header_size:
            return False
        if header.total_size > view_size:
            return False
        return True

    def _read_sensors(self, header: SharedMemHeader) -> tuple[list[tuple[int, int]], list[str]]:
        """Return the sensor table as parallel (id, instance) and display-name lists."""
        ids: list[tuple[int, int]] = []
        names: list[str] = []
        size = struct.calcsize(_SENSOR_FMT)
        for i in range(header.sensor_count):
            base = header.sensor_offset + i * header.sensor_element_size
            sid, inst, name_orig, name_user = struct.unpack(_SENSOR_FMT, self._read(base, size))
            ids.append((sid, inst))
            # A user-renamed sensor wins — that is the name shown in HWiNFO's UI.
            names.append(_cstr(name_user) or _cstr(name_orig))
        return ids, names

    def discover(self) -> list[HwinfoReading]:
        """Enumerate every reading currently published, with its latest value."""
        if not self._connected and not self._reopen():
            raise HwinfoUnavailable(self._last_error or _SHARED_MEMORY_HINT)

        try:
            return self._discover_locked()
        except (HwinfoUnavailable, struct.error, ValueError, IndexError) as e:
            # Layout shifted under us (HWiNFO restarted mid-read); one retry.
            logger.warning("Re-reading HWiNFO shared memory after error: %s", e)
            if not self._reopen():
                raise HwinfoUnavailable(self._last_error or str(e)) from e
            return self._discover_locked()

    def _discover_locked(self) -> list[HwinfoReading]:
        header = self._read_header()
        self._header = header

        sensor_ids, sensor_names = self._read_sensors(header)

        fmt = self._reading_fmt
        size = struct.calcsize(fmt)
        readings: list[HwinfoReading] = []
        row_by_triple: dict[tuple[int, int, int], int] = {}

        for i in range(header.reading_count):
            base = header.reading_offset + i * header.reading_element_size
            (
                rtype,
                sensor_index,
                reading_id,
                label_orig,
                label_user,
                unit,
                value,
                value_min,
                value_max,
                value_avg,
            ) = struct.unpack(fmt, self._read(base, size))

            if sensor_index < len(sensor_ids):
                sensor_id, sensor_instance = sensor_ids[sensor_index]
                sensor_name = sensor_names[sensor_index]
            else:
                # Orphaned row — keep it addressable rather than dropping it.
                sensor_id, sensor_instance = (0xFFFFFFFF, sensor_index)
                sensor_name = f"Unknown sensor {sensor_index}"

            reading = HwinfoReading(
                sensor_id=sensor_id,
                sensor_instance=sensor_instance,
                reading_id=reading_id,
                sensor_name=sensor_name,
                label=_cstr(label_user) or _cstr(label_orig),
                unit=_cstr(unit),
                reading_type=rtype,
                value=value,
                value_min=value_min,
                value_max=value_max,
                value_avg=value_avg,
            )
            readings.append(reading)
            row_by_triple[reading.triple] = i

        self._row_by_triple = row_by_triple
        self._sensor_ids = sensor_ids
        return readings

    def _sample_rows(self, triples: set[tuple[int, int, int]]) -> dict[tuple[int, int, int], float]:
        """Read just the bound rows' values, using the row map from the last scan.

        Far cheaper than a full enumeration — no string decoding, and only the
        selected rows are touched. Raises ``_LayoutChanged`` if a row no longer
        holds the reading it did, which forces the caller to re-enumerate.
        """
        header = self._header
        if header is None:
            raise HwinfoUnavailable("Shared memory is not open")

        out: dict[tuple[int, int, int], float] = {}
        for triple in triples:
            row = self._row_by_triple.get(triple)
            if row is None or row >= header.reading_count:
                raise _LayoutChanged(f"reading {triple} is no longer mapped")

            base = header.reading_offset + row * header.reading_element_size
            sensor_index, reading_id = struct.unpack("<II", self._read(base + 4, 8))
            if (
                reading_id != triple[2]
                or sensor_index >= len(self._sensor_ids)
                or self._sensor_ids[sensor_index] != (triple[0], triple[1])
            ):
                raise _LayoutChanged(f"row {row} no longer holds reading {triple}")

            (value,) = struct.unpack("<d", self._read(base + self._value_offset, 8))
            out[triple] = value
        return out

    # --- streaming ------------------------------------------------------

    def bind_channels(self, channels) -> None:
        """Record which HWiNFO reading each selected channel maps to.

        Called once at session start with the resolved ``ChannelDef`` list, so
        ``read_telemetry()`` can keep the engine's metric-key interface.
        """
        self._channel_triples = {
            ch.metric_key: (ch.sensor_id, ch.sensor_instance, ch.reading_id)
            for ch in channels
        }

    def read_telemetry(self, keys: list[str]) -> TelemetryList:
        """Sample the bound channels. Never raises — missing data reads as None.

        A dropped section (HWiNFO closed, or the free build's shared-memory
        timeout expiring) yields an all-None sample and a reconnect attempt on
        the next call, rather than tearing down the ATLAS session.
        """
        timestamp_ns = int(time.time() * 1e9)
        wanted = {t for t in (self._channel_triples.get(k) for k in keys) if t is not None}
        values: dict[tuple[int, int, int], float] = {}

        try:
            if not self._connected:
                raise _LayoutChanged("not connected")
            try:
                values = self._sample_rows(wanted)
            except _LayoutChanged:
                # Sensors came or went — re-enumerate, then read from the new map.
                for reading in self.discover():
                    if reading.triple in wanted:
                        values[reading.triple] = reading.value
        except (HwinfoUnavailable, _LayoutChanged, struct.error, ValueError, OSError) as e:
            if self._last_error != str(e):
                logger.warning("HWiNFO sample skipped: %s", e)
            self._last_error = str(e)
            self._reopen()

        result: dict[str, SampleValue] = {}
        for key in keys:
            triple = self._channel_triples.get(key)
            value = values.get(triple) if triple is not None else None
            result[key] = SampleValue(timestamp_ns, key, value)
        return TelemetryList(result)

    def get_session_info(self) -> dict[str, str]:
        info = {"host": "Unknown Host", "os": "Unknown OS", "hwinfo": "unknown"}
        try:
            info["host"] = socket.gethostname()
            info["os"] = platform.platform()
        except Exception as e:
            logger.warning("Error reading session info: %s", e)
        if self._header is not None:
            info["hwinfo"] = f"v{self._header.version} rev{self._header.revision}"
        return info
