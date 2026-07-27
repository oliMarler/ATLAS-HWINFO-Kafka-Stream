"""
Tests for the HWiNFO shared-memory parsing.

HWiNFO itself is not needed: each test builds a synthetic block in a named
Windows mapping and points the reader at it, which covers the parts most likely
to break — the two struct layouts, the stable-triple lookup, and the re-scan
that follows sensors being added or removed.

Run with pytest, or directly:  py backend/tests/test_hwinfo_reader.py
"""
import mmap
import os
import struct
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bridge.channel_registry import (
    build_channels,
    classify_sensor,
    normalize_unit,
    resolve_channels,
)
from bridge.hwinfo_reader import (
    READING_TYPE_FAN,
    READING_TYPE_TEMP,
    READING_TYPE_USAGE,
    HwinfoReader,
)

SIGNATURE = 0x53695748

# The three shapes the block has been observed in. "v2" is what HWiNFO 8.x
# publishes: the classic packed rows with a UTF-8 copy of the label/unit and
# sensor name appended, which makes the rows larger without moving any of the
# leading fields. "aligned" is the layout a natural reading of the published C
# would imply; no build is known to use it, but the reader still falls back to it.
_LAYOUTS = {
    #          header fmt        sensor fmt            reading fmt
    "v2":      ("<IIIqIIIIII",   "<II128s128s128s",    "<III128s128s16sdddd128s16s"),
    "classic": ("<IIIqIIIIII",   "<II128s128s",        "<III128s128s16sdddd"),
    "aligned": ("<III4xqIIIIII", "<II128s128s",        "<III128s128s16s4xdddd"),
}


def _b(text: str, width: int) -> bytes:
    raw = text.encode("latin-1")[: width - 1]
    return raw + b"\0" * (width - len(raw))


def _pack_sensor(fmt: str, sensor_id: int, instance: int, name: str) -> bytes:
    encoded = _b(name, 128)
    fields = [sensor_id, instance, encoded, _b("", 128)]
    if fmt.count("128s") == 3:  # v2 appends a UTF-8 name
        fields.append(encoded)
    return struct.pack(fmt, *fields)


def _pack_reading(fmt: str, rtype, sensor_index, reading_id, label, unit, value) -> bytes:
    encoded_label, encoded_unit = _b(label, 128), _b(unit, 16)
    fields = [
        rtype, sensor_index, reading_id,
        encoded_label, _b("", 128), encoded_unit,
        value, value, value, value,
    ]
    if fmt.endswith("128s16s"):  # v2 appends a UTF-8 label and unit
        fields += [encoded_label, encoded_unit]
    return struct.pack(fmt, *fields)


def build_block(sensors, readings, layout="v2") -> bytes:
    """Assemble a shared-memory image in one of HWiNFO's block layouts.

    ``sensors``  — [(sensor_id, instance, name), ...]
    ``readings`` — [(type, sensor_index, reading_id, label, unit, value), ...]
    """
    header_fmt, sensor_fmt, reading_fmt = _LAYOUTS[layout]
    header_size = struct.calcsize(header_fmt)
    sensor_size = struct.calcsize(sensor_fmt)
    reading_size = struct.calcsize(reading_fmt)

    sensor_offset = header_size
    reading_offset = sensor_offset + sensor_size * len(sensors)

    header = struct.pack(
        header_fmt,
        SIGNATURE,
        2 if layout == "v2" else 1,
        1 if layout == "v2" else 0,
        int(time.time()),
        sensor_offset,
        sensor_size,
        len(sensors),
        reading_offset,
        reading_size,
        len(readings),
    )

    sensor_bytes = b"".join(_pack_sensor(sensor_fmt, *s) for s in sensors)
    reading_bytes = b"".join(_pack_reading(reading_fmt, *r) for r in readings)
    return header + sensor_bytes + reading_bytes


class FakeSharedMemory:
    """A named mapping that stands in for HWiNFO's, for the duration of a test.

    Sized with headroom so a test can swap in a larger sensor tree, the way
    HWiNFO does when hardware appears.
    """

    CAPACITY = 256 * 1024

    def __init__(self, name: str, payload: bytes) -> None:
        self.name = name
        self._mm = mmap.mmap(-1, max(len(payload), self.CAPACITY), tagname=name)
        self._mm.write(payload)

    def replace(self, payload: bytes) -> None:
        """Rewrite in place — mimics HWiNFO refreshing values or re-ordering rows."""
        self._mm.seek(0)
        self._mm.write(payload)

    def close(self) -> None:
        self._mm.close()


SENSORS = [
    (0xF0000100, 0, "CPU [#0]: AMD Ryzen 9 7950X: Enhanced"),
    (0xF0000200, 0, "GPU [#0]: NVIDIA GeForce RTX 4090"),
]

READINGS = [
    (READING_TYPE_USAGE, 0, 1, "Total CPU Usage", "%", 37.5),
    (READING_TYPE_TEMP, 0, 2, "CPU (Tctl/Tdie)", "\xb0C", 64.25),
    (READING_TYPE_FAN, 0, 3, "CPU Fan", "RPM", 1180.0),
    (READING_TYPE_TEMP, 1, 1, "GPU Temperature", "\xb0C", 51.0),
    (READING_TYPE_USAGE, 1, 2, "GPU Core Load", "%", 8.0),
]


def _reader_for(payload: bytes, name: str):
    shm = FakeSharedMemory(name, payload)
    reader = HwinfoReader(shared_mem_name=name)
    assert reader.connect(), reader.last_error
    return shm, reader


def _assert_readings_decode(reader):
    readings = reader.discover()
    assert len(readings) == 5

    cpu_temp = next(r for r in readings if r.label == "CPU (Tctl/Tdie)")
    assert cpu_temp.value == 64.25
    assert cpu_temp.sensor_name.startswith("CPU [#0]")
    assert cpu_temp.triple == (0xF0000100, 0, 2)
    assert cpu_temp.unit == "\xb0C"

    assert next(r for r in readings if r.label == "CPU Fan").value == 1180.0
    gpu_load = next(r for r in readings if r.label == "GPU Core Load")
    assert gpu_load.value == 8.0
    assert gpu_load.sensor_name.startswith("GPU [#0]")
    return readings


def test_parses_v2_layout():
    """The block HWiNFO 8.x actually publishes: 460-byte rows, 392-byte sensors.

    Guards the failure that shipped in v1.0.0 — the larger rows were parsed with
    the 4-byte-padded prefix, which reads every value one field late. Labels sit
    before the values, so the channels looked perfectly healthy in ATLAS while
    every trace was flat zero.
    """
    payload = build_block(SENSORS, READINGS, layout="v2")
    shm, reader = _reader_for(payload, "Local\\TestHWiNFO_v2")
    try:
        assert reader.header.version == 2
        assert reader.header.reading_element_size == 460
        assert reader.header.sensor_element_size == 392
        _assert_readings_decode(reader)
    finally:
        reader.disconnect()
        shm.close()


def test_parses_classic_packed_layout():
    payload = build_block(SENSORS, READINGS, layout="classic")
    shm, reader = _reader_for(payload, "Local\\TestHWiNFO_classic")
    try:
        assert reader.header.reading_element_size == 316
        _assert_readings_decode(reader)
    finally:
        reader.disconnect()
        shm.close()


def test_parses_aligned_layout():
    """The padded layout the published C implies, kept as a fallback."""
    payload = build_block(SENSORS, READINGS, layout="aligned")
    shm, reader = _reader_for(payload, "Local\\TestHWiNFO_aligned")
    try:
        assert reader.header.reading_element_size == 320
        _assert_readings_decode(reader)
    finally:
        reader.disconnect()
        shm.close()


def test_header_layout_chosen_by_table_adjacency():
    """A header decoded with the wrong format must be rejected, not tolerated.

    Both candidates can look individually plausible; only the correct one has the
    sensor table ending exactly where the reading table starts.
    """
    for layout, expected_sensor_size in (("v2", 392), ("classic", 264), ("aligned", 264)):
        shm, reader = _reader_for(
            build_block(SENSORS, READINGS, layout=layout), f"Local\\TestHWiNFO_hdr_{layout}"
        )
        try:
            header = reader.header
            assert header.sensor_element_size == expected_sensor_size, layout
            assert (
                header.sensor_offset + header.sensor_element_size * header.sensor_count
                == header.reading_offset
            ), layout
        finally:
            reader.disconnect()
            shm.close()


def test_channels_track_readings_across_reorder():
    """Rows moving must not silently repoint a channel at a different sensor."""
    shm, reader = _reader_for(build_block(SENSORS, READINGS), "Local\\TestHWiNFO_reorder")
    try:
        channels = build_channels(reader.discover(), frequency=2)
        reader.bind_channels(channels)
        keys = [c.metric_key for c in channels]

        first = reader.read_telemetry(keys).parameter_values
        fan_key = next(c.metric_key for c in channels if c.label == "CPU Fan")
        gpu_temp_key = next(c.metric_key for c in channels if c.label == "GPU Temperature")
        assert first[fan_key].value == 1180.0
        assert first[gpu_temp_key].value == 51.0

        # A drive wakes up: a new sensor is prepended and every row shifts.
        new_sensors = [(0xF0000300, 0, "Drive [#0]: Samsung 990 PRO")] + SENSORS
        new_readings = [(READING_TYPE_TEMP, 0, 1, "Drive Temperature", "\xb0C", 41.0)] + [
            (rtype, idx + 1, rid, label, unit, value + 1.0)
            for rtype, idx, rid, label, unit, value in READINGS
        ]
        shm.replace(build_block(new_sensors, new_readings))

        second = reader.read_telemetry(keys).parameter_values
        # Values follow the reading, not the row it used to occupy.
        assert second[fan_key].value == 1181.0
        assert second[gpu_temp_key].value == 52.0
    finally:
        reader.disconnect()
        shm.close()


def test_missing_shared_memory_is_not_fatal():
    """Losing HWiNFO mid-session yields empty samples, not an exception."""
    reader = HwinfoReader(shared_mem_name="Local\\TestHWiNFO_does_not_exist")
    assert not reader.connect()
    assert reader.last_error
    telemetry = reader.read_telemetry(["AnyKey"]).parameter_values
    assert telemetry["AnyKey"].value is None


def test_channel_naming_and_presets():
    shm, reader = _reader_for(build_block(SENSORS, READINGS), "Local\\TestHWiNFO_naming")
    try:
        channels = build_channels(reader.discover(), frequency=2)
        by_label = {c.label: c for c in channels}

        assert by_label["Total CPU Usage"].metric_key == "CPU0_TotalCPUUsage"
        assert by_label["GPU Temperature"].metric_key == "GPU0_GPUTemperature"
        # Degree signs do not survive into ATLAS parameter units.
        assert by_label["CPU (Tctl/Tdie)"].units == "C"
        assert by_label["CPU Fan"].units == "RPM"
        assert by_label["CPU Fan"].max_value == 8000

        temps = resolve_channels(channels, preset="temperatures")
        assert {c.label for c in temps} == {"CPU (Tctl/Tdie)", "GPU Temperature"}

        gpu = resolve_channels(channels, preset="gpu")
        assert {c.label for c in gpu} == {"GPU Temperature", "GPU Core Load"}

        essential = resolve_channels(channels, preset="essential")
        assert "Total CPU Usage" in {c.label for c in essential}
        assert "GPU Core Load" in {c.label for c in essential}

        custom = resolve_channels(channels, custom_keys=["GPU0_GPUCoreLoad"])
        assert [c.label for c in custom] == ["GPU Core Load"]
    finally:
        reader.disconnect()
        shm.close()


def test_duplicate_labels_get_distinct_keys():
    """Two identically-named fan headers must not collide into one ATLAS channel."""
    readings = [
        (READING_TYPE_FAN, 0, 10, "Fan", "RPM", 900.0),
        (READING_TYPE_FAN, 0, 11, "Fan", "RPM", 1500.0),
    ]
    shm, reader = _reader_for(build_block(SENSORS[:1], readings), "Local\\TestHWiNFO_dupes")
    try:
        channels = build_channels(reader.discover(), frequency=2)
        keys = [c.metric_key for c in channels]
        assert len(set(keys)) == 2
        # No "_Fan_Fan" — the label already names the type, so a number is used.
        assert keys == ["CPU0_Fan", "CPU0_Fan_2"]
    finally:
        reader.disconnect()
        shm.close()


def test_same_label_on_different_reading_types_is_qualified():
    """MSI boards label both a temperature and a fan header plain "CPU"."""
    readings = [
        (READING_TYPE_TEMP, 0, 20, "CPU", "\xb0C", 44.0),
        (READING_TYPE_FAN, 0, 21, "CPU", "RPM", 1013.0),
    ]
    shm, reader = _reader_for(build_block(SENSORS[:1], readings), "Local\\TestHWiNFO_sametype")
    try:
        channels = build_channels(reader.discover(), frequency=2)
        assert [c.metric_key for c in channels] == ["CPU0_CPU", "CPU0_CPU_Fan"]
    finally:
        reader.disconnect()
        shm.close()


def test_board_model_containing_wifi_is_not_a_network_sensor():
    """"ROG STRIX X670E-E GAMING WIFI" is a mainboard, not a network adapter."""
    assert classify_sensor("ASUS ROG STRIX X670E-E GAMING WIFI (Nuvoton NCT6799D)") == "motherboard"
    assert classify_sensor("Network: Intel Ethernet Controller I225-V") == "network"
    assert classify_sensor("GPU [#0]: NVIDIA GeForce RTX 4090") == "gpu"
    assert classify_sensor("CPU [#0]: AMD Ryzen 9 7950X") == "cpu"
    assert classify_sensor("Drive [#0]: Samsung SSD 990 PRO") == "drives"


def test_motherboard_preset_collects_board_sensors():
    sensors = [(0xF0000300, 0, "ASUS ROG STRIX X670E-E GAMING WIFI (Nuvoton NCT6799D)")]
    readings = [
        (READING_TYPE_FAN, 0, 1, "Chassis Fan 1", "RPM", 880.0),
        (READING_TYPE_TEMP, 0, 2, "VRM", "\xb0C", 52.0),
        (READING_TYPE_USAGE, 0, 3, "Physical Memory Load", "%", 46.0),
    ]
    shm, reader = _reader_for(build_block(sensors, readings), "Local\\TestHWiNFO_board")
    try:
        channels = build_channels(reader.discover(), frequency=2)
        assert len(resolve_channels(channels, preset="motherboard")) == 3
        assert resolve_channels(channels, preset="network") == []
        # Memory is matched on the label, since it has no sensor of its own.
        memory = resolve_channels(channels, preset="memory")
        assert [c.label for c in memory] == ["Physical Memory Load"]
    finally:
        reader.disconnect()
        shm.close()


def test_normalize_unit():
    assert normalize_unit("\xb0C") == "C"
    assert normalize_unit("\xb0F") == "F"
    assert normalize_unit("RPM") == "RPM"
    assert normalize_unit("Yes/No") == "Yes/No"


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if not name.startswith("test_") or not callable(fn):
            continue
        try:
            fn()
            print(f"PASS  {name}")
        except AssertionError as e:
            failures += 1
            print(f"FAIL  {name}: {e}")
        except Exception as e:
            failures += 1
            print(f"ERROR {name}: {e!r}")
    print(f"\n{'FAILED' if failures else 'OK'} ({failures} failure(s))")
    sys.exit(1 if failures else 0)
