"""
Turns HWiNFO readings into ATLAS channel definitions.

Unlike a fixed hardware probe, the channel set here is only known once HWiNFO's
shared memory has been read: which sensors exist depends on the machine, the
motherboard's chipset, which drives are awake, and what the user has hidden in
HWiNFO's own UI. ``build_channels()`` is therefore called at bridge-start time
from ``bridge_engine.py``, not at import.

Presets are predicates over the discovered set rather than fixed key lists, for
the same reason — "all temperatures" has to mean whatever this machine reports.
"""
import logging
import re
from dataclasses import dataclass

from bridge.hwinfo_reader import (
    READING_TYPE_CLOCK,
    READING_TYPE_FAN,
    READING_TYPE_OTHER,
    READING_TYPE_POWER,
    READING_TYPE_TEMP,
    READING_TYPE_USAGE,
    READING_TYPE_VOLT,
    HwinfoReading,
)

logger = logging.getLogger(__name__)

ATLAS_APP = "HWiNFO"
ATLAS_GROUP = "HWiNFO"

# Channel counts above this make session start noticeably slow: ATLAS requires
# one GetParameterDataFormatId round-trip per parameter (see CLAUDE.md rule 2).
CHANNEL_COUNT_WARNING = 250


@dataclass
class ChannelDef:
    metric_key: str
    atlas_identifier: str
    atlas_name: str
    atlas_app: str
    units: str
    description: str
    format_string: str
    min_value: float
    max_value: float
    frequency: int
    group: str
    # HWiNFO identity — the stable triple used to re-find this reading each poll
    sensor_id: int = 0
    sensor_instance: int = 0
    reading_id: int = 0
    reading_type: int = READING_TYPE_OTHER
    label: str = ""
    sensor_name: str = ""
    # True for channels computed by derived_channels.py rather than read from
    # HWiNFO — the sensor/reading fields above are meaningless for these, so
    # bridge_engine must not hand them to HwinfoReader.bind_channels().
    is_derived: bool = False


# --- naming ---------------------------------------------------------------

_NON_ALNUM = re.compile(r"[^0-9A-Za-z]+")
_PARENTHETICAL = re.compile(r"\(.*?\)")

_UNIT_REWRITES = {
    "°C": "C",
    "°F": "F",
    "µs": "us",
    "µV": "uV",
    "µA": "uA",
    "Ω": "Ohm",
}


def _slug(text: str) -> str:
    """Build a CamelCase identifier fragment from arbitrary sensor text."""
    parts = [p for p in _NON_ALNUM.split(text) if p]
    out = []
    for part in parts:
        out.append(part if part[0].isupper() or part[0].isdigit() else part[0].upper() + part[1:])
    return "".join(out)


def _sensor_slug(sensor_name: str) -> str:
    """Compact a sensor name like 'CPU [#0]: AMD Ryzen 9 7950X' down to 'CPU0'."""
    head = sensor_name.split(":", 1)[0]
    head = _PARENTHETICAL.sub("", head)
    return _slug(head)[:24] or "Sensor"


def normalize_unit(unit: str) -> str:
    """ATLAS parameter units are plain strings, so drop the non-ASCII glyphs."""
    for src, dst in _UNIT_REWRITES.items():
        unit = unit.replace(src, dst)
    return unit.encode("ascii", "ignore").decode("ascii").strip()


# --- ranges and formatting -------------------------------------------------

_UNIT_RANGES: dict[str, tuple[float, float]] = {
    "C": (0, 120),
    "F": (32, 250),
    "V": (0, 24),
    "mV": (0, 2000),
    "RPM": (0, 8000),
    "W": (0, 1000),
    "A": (0, 256),
    "MHz": (0, 8000),
    "GHz": (0, 8),
    "%": (0, 100),
    "Yes/No": (0, 1),
    "GB": (0, 1024),
    "MB": (0, 131072),
    "KB": (0, 1048576),
    "MB/s": (0, 16000),
    "GB/s": (0, 128),
    "GT/s": (0, 128),
    "FPS": (0, 1000),
    "ms": (0, 1000),
    "us": (0, 100000),
    "x": (0, 100),
}

_TYPE_RANGES: dict[int, tuple[float, float]] = {
    READING_TYPE_TEMP: (0, 120),
    READING_TYPE_VOLT: (0, 24),
    READING_TYPE_FAN: (0, 8000),
    READING_TYPE_POWER: (0, 1000),
    READING_TYPE_CLOCK: (0, 8000),
    READING_TYPE_USAGE: (0, 100),
}


def _range_for(reading: HwinfoReading, unit: str) -> tuple[float, float]:
    if unit in _UNIT_RANGES:
        return _UNIT_RANGES[unit]
    if reading.reading_type in _TYPE_RANGES:
        return _TYPE_RANGES[reading.reading_type]
    # Unknown quantity — give it a range wide enough not to clip the trace.
    return (0.0, 10000.0)


def _format_for(reading: HwinfoReading, unit: str, hi: float) -> str:
    if hi <= 1:
        return "%3.0f"
    if reading.reading_type == READING_TYPE_VOLT or unit in ("V", "GHz"):
        return "%6.3f"
    if reading.reading_type in (READING_TYPE_FAN, READING_TYPE_CLOCK) or unit in ("RPM", "MHz"):
        return "%6.0f"
    if reading.reading_type in (READING_TYPE_TEMP, READING_TYPE_USAGE) or unit in ("C", "%"):
        return "%5.1f"
    if reading.reading_type == READING_TYPE_POWER or unit == "W":
        return "%6.1f"
    if hi >= 10000:
        return "%9.0f"
    return "%8.2f"


# --- construction ----------------------------------------------------------


def build_channels(readings: list[HwinfoReading], frequency: int = 2) -> list[ChannelDef]:
    """Map every discovered HWiNFO reading onto an ATLAS channel definition.

    Metric keys are derived from the sensor and reading labels so they stay
    readable in ATLAS, and de-duplicated with a numeric suffix — HWiNFO happily
    reports the same label twice under one sensor (two identical fan headers,
    say), and duplicate ATLAS identifiers would collide silently.
    """
    channels: list[ChannelDef] = []
    used_keys: set[str] = set()

    for reading in readings:
        label = reading.label or f"Reading {reading.reading_id}"
        unit = normalize_unit(reading.unit)
        lo, hi = _range_for(reading, unit)

        base_key = f"{_sensor_slug(reading.sensor_name)}_{_slug(label)[:48]}"
        key = base_key
        if key in used_keys:
            # Boards routinely label a temperature and a fan header identically
            # ("CPU" on MSI), so qualify by reading type — "..._CPU_Fan" says far
            # more in ATLAS than "..._CPU_2". Skipped when the label already names
            # the type, which would only produce "..._Fan_Fan".
            stem = base_key
            if reading.type_name.lower() not in label.lower():
                stem = f"{base_key}_{reading.type_name}"
            key = stem
            suffix = 2
            while key in used_keys:
                key = f"{stem}_{suffix}"
                suffix += 1
        used_keys.add(key)

        description = f"{reading.sensor_name} - {label}"
        if unit:
            description += f" ({unit})"

        channels.append(
            ChannelDef(
                metric_key=key,
                atlas_identifier=f"{key}:{ATLAS_APP}",
                atlas_name=key,
                atlas_app=ATLAS_APP,
                units=unit,
                description=description,
                format_string=_format_for(reading, unit, hi),
                min_value=lo,
                max_value=hi,
                frequency=frequency,
                group=reading.sensor_name or "Unknown",
                sensor_id=reading.sensor_id,
                sensor_instance=reading.sensor_instance,
                reading_id=reading.reading_id,
                reading_type=reading.reading_type,
                label=label,
                sensor_name=reading.sensor_name,
            )
        )

    logger.info("Built %d channels from %d HWiNFO readings", len(channels), len(readings))
    return channels


# --- presets ---------------------------------------------------------------

_GPU_SENSOR_RE = re.compile(r"\bgpu\b|geforce|radeon|nvidia|\barc\b", re.I)
_CPU_SENSOR_RE = re.compile(r"\bcpu\b|\bryzen\b|\bxeon\b|core\s*i\d", re.I)
_DRIVE_SENSOR_RE = re.compile(r"\bdrive\b|\bnvme\b|\bssd\b|\bhdd\b|s\.m\.a\.r\.t|\bdisk\b", re.I)
# Mainboard sensors are named after the board and its Super-I/O chip. This has to
# be tested before the network rule: plenty of boards ship "WIFI" in the model
# name ("ROG STRIX X670E-E GAMING WIFI") and would otherwise be filed as network
# adapters, emptying the motherboard group entirely.
_BOARD_SENSOR_RE = re.compile(
    r"motherboard|mainboard|nuvoton|fintek|winbond|smsc|\bnct\d|\bite\s+it\d"
    r"|^asus|^msi|^gigabyte|^asrock|^biostar|^supermicro|^nzxt",
    re.I,
)
_NETWORK_SENSOR_RE = re.compile(r"\bnetwork\b|ethernet|wi-?fi|\bnic\b", re.I)

# Memory readings live under whichever sensor owns them rather than a sensor of
# their own, so this group is matched on the reading label.
_MEMORY_LABEL_RE = re.compile(r"\bmemory\b|\bdimm\b|\bram\b|page file", re.I)

_SENSOR_CATEGORIES: list[tuple[str, re.Pattern]] = [
    ("gpu", _GPU_SENSOR_RE),
    ("cpu", _CPU_SENSOR_RE),
    ("drives", _DRIVE_SENSOR_RE),
    ("motherboard", _BOARD_SENSOR_RE),
    ("network", _NETWORK_SENSOR_RE),
]


def classify_sensor(sensor_name: str) -> str:
    """Assign a sensor to exactly one hardware category, first match winning."""
    for category, pattern in _SENSOR_CATEGORIES:
        if pattern.search(sensor_name):
            return category
    return "other"


def _in_category(channels: list[ChannelDef], category: str) -> list[ChannelDef]:
    return [c for c in channels if classify_sensor(c.sensor_name) == category]


def _by_type(channels: list[ChannelDef], reading_type: int) -> list[ChannelDef]:
    return [c for c in channels if c.reading_type == reading_type]


# Ordered label matchers for the 'essential' preset. Each contributes at most one
# channel, so the preset stays small on machines with rich sensor trees.
#
# Vendors name the same quantity quite differently — AMD reports "GPU ASIC Power"
# where NVIDIA reports "GPU Power", and MSI labels its CPU fan header plain "CPU"
# rather than "CPU Fan" — so these patterns carry the known variants. Where a
# sensor reports both an aggregate and its parts, the aggregate is matched first
# ("GPU ASIC Power" ahead of "GPU Core Power").
_ESSENTIAL_MATCHERS: list[tuple[re.Pattern, int | None]] = [
    (re.compile(r"^total cpu usage$|^cpu utility$", re.I), READING_TYPE_USAGE),
    (re.compile(r"cpu \(tctl|^cpu package$|^core max$|^cpu temperature$", re.I), READING_TYPE_TEMP),
    (re.compile(r"cpu package power|^cpu package \(smu\)$|^cpu ppt$", re.I), READING_TYPE_POWER),
    (re.compile(r"average effective clock|^cpu clock$|^core 0 clock$", re.I), READING_TYPE_CLOCK),
    (re.compile(r"gpu core load|gpu utilization|^gpu load$", re.I), READING_TYPE_USAGE),
    (re.compile(r"^gpu temperature$|gpu hot ?spot", re.I), READING_TYPE_TEMP),
    (
        re.compile(
            r"gpu (?:asic|board|total|package) power|total graphics power|^gpu power$|gpu ppt",
            re.I,
        ),
        READING_TYPE_POWER,
    ),
    (re.compile(r"^gpu clock$|gpu core clock", re.I), READING_TYPE_CLOCK),
    (re.compile(r"^gpu memory (?:usage|used|allocated)$|dedicated video memory", re.I), None),
    (re.compile(r"^physical memory (used|load)$|^memory usage$", re.I), None),
    (re.compile(r"^virtual memory (used|load|committed)$", re.I), None),
    (re.compile(r"^cpu[ _-]?fan$|^cpu$|cpu.?fan|^fan\s*1$", re.I), READING_TYPE_FAN),
]


def _essential(channels: list[ChannelDef]) -> list[ChannelDef]:
    picked: list[ChannelDef] = []
    seen: set[str] = set()
    for pattern, reading_type in _ESSENTIAL_MATCHERS:
        for ch in channels:
            if ch.metric_key in seen:
                continue
            if reading_type is not None and ch.reading_type != reading_type:
                continue
            if pattern.search(ch.label):
                picked.append(ch)
                seen.add(ch.metric_key)
                break
    return picked


def _motherboard(channels: list[ChannelDef]) -> list[ChannelDef]:
    """Mainboard sensors, plus anything that matched no category at all."""
    return [
        c for c in channels if classify_sensor(c.sensor_name) in ("motherboard", "other")
    ]


PRESET_BUILDERS = {
    "essential": _essential,
    "cpu": lambda chs: _in_category(chs, "cpu"),
    "gpu": lambda chs: _in_category(chs, "gpu"),
    "memory": lambda chs: [c for c in chs if _MEMORY_LABEL_RE.search(c.label)],
    "drives": lambda chs: _in_category(chs, "drives"),
    "network": lambda chs: _in_category(chs, "network"),
    "motherboard": _motherboard,
    "temperatures": lambda chs: _by_type(chs, READING_TYPE_TEMP),
    "fans": lambda chs: _by_type(chs, READING_TYPE_FAN),
    "power": lambda chs: _by_type(chs, READING_TYPE_POWER),
    "clocks": lambda chs: _by_type(chs, READING_TYPE_CLOCK),
    "voltages": lambda chs: _by_type(chs, READING_TYPE_VOLT),
    "usage": lambda chs: _by_type(chs, READING_TYPE_USAGE),
    "full": lambda chs: list(chs),
}

PRESET_DESCRIPTIONS = {
    "essential": "Curated summary - CPU/GPU load, temperature, power, clock, memory, fan",
    "cpu": "Everything reported by the CPU sensors",
    "gpu": "Everything reported by the GPU sensors",
    "memory": "System and video memory readings, wherever they are reported",
    "drives": "Drive temperatures, activity and S.M.A.R.T. values",
    "network": "Network adapter sensors",
    "motherboard": "Mainboard sensors, plus anything uncategorised",
    "temperatures": "All temperature readings",
    "fans": "All fan speed readings",
    "power": "All power readings",
    "clocks": "All clock readings",
    "voltages": "All voltage readings",
    "usage": "All usage/load readings",
    "full": "Every reading HWiNFO publishes (slow to start - watch the channel count)",
}


def preset_names() -> list[str]:
    return list(PRESET_BUILDERS.keys())


def apply_preset(channels: list[ChannelDef], preset: str) -> list[ChannelDef]:
    builder = PRESET_BUILDERS.get(preset)
    if builder is None:
        logger.warning("Unknown preset %r, falling back to 'essential'", preset)
        builder = PRESET_BUILDERS["essential"]
    return builder(channels)


def resolve_channels(
    channels: list[ChannelDef],
    preset: str | None = None,
    custom_keys: list[str] | None = None,
) -> list[ChannelDef]:
    """Narrow the discovered channel set to what this session should stream."""
    if custom_keys:
        by_key = {c.metric_key: c for c in channels}
        return [by_key[k] for k in custom_keys if k in by_key]
    return apply_preset(channels, preset or "essential")


def get_groups(channels: list[ChannelDef]) -> list[str]:
    """Distinct sensor names, in first-seen order — used for UI grouping only.

    ATLAS itself gets exactly one GroupDefinition (see CLAUDE.md rule 3); this
    grouping never reaches the ConfigurationPacket.
    """
    seen: set[str] = set()
    groups: list[str] = []
    for ch in channels:
        if ch.group not in seen:
            seen.add(ch.group)
            groups.append(ch.group)
    return groups
