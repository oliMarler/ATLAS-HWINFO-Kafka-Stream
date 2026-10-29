"""
Plain-English findings from a snapshot of HWiNFO channel values.

HWiNFO reports throttling as explicit Yes/No readings ("Core Thermal Throttling",
"Power Limit Exceeded", "PerfCap Reason - Thermal" and friends), which is far more
direct than inferring a limit from a clock dropping. Those flags drive most of the
findings below; thresholds only cover what HWiNFO does not state outright.

Channel keys are machine-specific, so everything matches on the reading label and
type carried in the ``ChannelDef`` rather than on fixed key names.
"""
import re

from bridge.channel_registry import ChannelDef
from bridge.hwinfo_reader import (
    READING_TYPE_FAN,
    READING_TYPE_TEMP,
    READING_TYPE_USAGE,
)

CPU_TEMP_WARN_C = 90.0
CPU_TEMP_CRITICAL_C = 95.0
GPU_TEMP_WARN_C = 83.0
GPU_HOTSPOT_DELTA_WARN_C = 20.0
LOAD_HIGH_PCT = 90.0
LOAD_IDLE_PCT = 40.0
MEMORY_HIGH_PCT = 90.0
FAN_STALLED_RPM = 1.0
FAN_STALL_TEMP_C = 60.0
LIMIT_REACHED_PCT = 99.0      # a limit reading given as % of the limit (Ryzen PPT/TDC/EDC)

_THROTTLE_FLAGS = [
    (re.compile(r"thermal throttling", re.I), "critical", "Thermal throttling active"),
    (re.compile(r"power limit exceeded|ppt limit|package power limit", re.I), "warning", "Power limit reached"),
    (re.compile(r"current limit|tdc limit|edc limit", re.I), "warning", "Current limit reached"),
    (re.compile(r"voltage.*limit|vrm.*throttl", re.I), "warning", "VRM limit reached"),
    (re.compile(r"perfcap reason - thermal", re.I), "critical", "GPU capped by temperature"),
    (re.compile(r"perfcap reason - power", re.I), "warning", "GPU capped by power limit"),
    (re.compile(r"perfcap reason - (voltage|reliability|util)", re.I), "info", "GPU performance capped"),
    (re.compile(r"critical temperature", re.I), "critical", "Critical temperature reported"),
]

_CPU_TEMP_RE = re.compile(r"cpu \(tctl|^cpu package$|^core max$|^cpu temperature$", re.I)
_GPU_TEMP_RE = re.compile(r"^gpu temperature$", re.I)
_GPU_HOTSPOT_RE = re.compile(r"gpu hot ?spot", re.I)
_CPU_LOAD_RE = re.compile(r"^total cpu usage$|^cpu utility$", re.I)
_GPU_LOAD_RE = re.compile(r"gpu core load|gpu utilization|^gpu load$", re.I)
_MEMORY_LOAD_RE = re.compile(r"^physical memory load$|^memory usage$", re.I)


def _first(
    values: dict[str, float],
    channels: list[ChannelDef],
    pattern: re.Pattern,
    reading_type: int | None = None,
) -> float | None:
    for ch in channels:
        if reading_type is not None and ch.reading_type != reading_type:
            continue
        if pattern.search(ch.label) and ch.metric_key in values:
            return values[ch.metric_key]
    return None


def analyze(values: dict[str, float], channels: list[ChannelDef]) -> list[dict[str, str]]:
    insights: list[dict[str, str]] = []
    seen: set[str] = set()

    def add(level: str, message: str) -> None:
        if message not in seen:
            seen.add(message)
            insights.append({"level": level, "message": message})

    # HWiNFO's own throttle/limit flags come first — they are statements of fact,
    # not inferences from a threshold. A Yes/No flag is set at 1. Ryzen's
    # "CPU PPT Limit" / "TDC Limit" / "EDC Limit" are percentages of the limit
    # in use (30 % at idle), so those count only when the limit is reached.
    for ch in channels:
        value = values.get(ch.metric_key)
        if value is None or value < (LIMIT_REACHED_PCT if ch.units == "%" else 1):
            continue
        for pattern, level, message in _THROTTLE_FLAGS:
            if pattern.search(ch.label):
                add(level, f"{message} ({ch.sensor_name.split(':', 1)[0].strip()})")
                break

    cpu_temp = _first(values, channels, _CPU_TEMP_RE, READING_TYPE_TEMP)
    gpu_temp = _first(values, channels, _GPU_TEMP_RE, READING_TYPE_TEMP)
    hotspot = _first(values, channels, _GPU_HOTSPOT_RE, READING_TYPE_TEMP)
    cpu_load = _first(values, channels, _CPU_LOAD_RE, READING_TYPE_USAGE)
    gpu_load = _first(values, channels, _GPU_LOAD_RE, READING_TYPE_USAGE)
    memory_load = _first(values, channels, _MEMORY_LOAD_RE)

    if cpu_temp is not None:
        if cpu_temp >= CPU_TEMP_CRITICAL_C:
            add("critical", f"CPU running hot ({cpu_temp:.0f} C)")
        elif cpu_temp >= CPU_TEMP_WARN_C:
            add("warning", f"CPU temperature climbing ({cpu_temp:.0f} C)")

    if gpu_temp is not None and gpu_temp >= GPU_TEMP_WARN_C:
        add("warning", f"GPU temperature climbing ({gpu_temp:.0f} C)")

    if hotspot is not None and gpu_temp is not None:
        delta = hotspot - gpu_temp
        if delta >= GPU_HOTSPOT_DELTA_WARN_C:
            add(
                "warning",
                f"Large GPU hotspot delta ({delta:.0f} C) - check mounting pressure or paste",
            )

    if cpu_load is not None and gpu_load is not None:
        if cpu_load >= LOAD_HIGH_PCT and gpu_load <= LOAD_IDLE_PCT:
            add("info", "CPU-bound - GPU has headroom")
        elif gpu_load >= LOAD_HIGH_PCT and cpu_load <= LOAD_IDLE_PCT:
            add("info", "GPU-bound - CPU has headroom")
        elif cpu_load >= LOAD_HIGH_PCT and gpu_load >= LOAD_HIGH_PCT:
            add("warning", "Both CPU and GPU near full load")

    if memory_load is not None and memory_load >= MEMORY_HIGH_PCT:
        add("warning", f"Memory pressure ({memory_load:.0f}% used)")

    hottest = max(
        (
            values[ch.metric_key]
            for ch in channels
            if ch.reading_type == READING_TYPE_TEMP and ch.metric_key in values
        ),
        default=None,
    )
    if hottest is not None and hottest >= FAN_STALL_TEMP_C:
        for ch in channels:
            if ch.reading_type != READING_TYPE_FAN:
                continue
            rpm = values.get(ch.metric_key)
            if rpm is not None and rpm < FAN_STALLED_RPM:
                add("warning", f"{ch.label} is stopped while temperatures are elevated")

    if not insights:
        add("info", "All readings within normal limits")

    return insights
