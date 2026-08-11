# ATLAS HWiNFO Kafka Stream

Stream live hardware sensor data from [HWiNFO](https://www.hwinfo.com/) into
[Motion Applied ATLAS](https://atlas.motionapplied.com/), via Kafka and the MA Data
Platforms Stream API.

HWiNFO exposes several hundred readings on a typical machine — per-core clocks
and temperatures, VRM and package power, fan headers, drive S.M.A.R.T. values,
GPU hotspot deltas, and explicit throttling flags. This bridge turns any subset
of them into ATLAS parameters so they can be plotted, overlaid and analysed like
any other telemetry.

```
HWiNFO64 (Global\HWiNFO_SENS_SM2)
    → Python bridge
    → gRPC Stream API (:13579)
    → Kafka (:9092)
    → ATLAS Stream Recorder
```

## Documentation

- **[MANUAL.md](MANUAL.md)** — the full manual: HWiNFO setup, every preset and
  control, how channels are named in ATLAS, the HTTP API, troubleshooting.
- [GETTING_STARTED.md](GETTING_STARTED.md) — the short path from nothing to a
  live trace.
- [CLAUDE.md](CLAUDE.md) — implementation constraints and hard-won lessons, for
  anyone changing the code.

## Requirements

- **Windows** — HWiNFO's shared memory is a Windows section, accessed here via `OpenFileMappingW`
- **HWiNFO64**, running, with **Settings → Main Settings → Shared Memory Support** ticked
- **Docker Desktop** — runs Kafka, the Stream API and the Key Generator
- **Python 3.10+**
- **ATLAS 10** with the Stream Recorder, to view the data

> On the free HWiNFO build, Shared Memory Support switches itself off after
> 12 hours of runtime; restart HWiNFO to bring it back. The Pro licence removes
> the limit.

## Quick start

```bash
scripts\start.bat
```

That brings up Docker, installs the Python dependencies and serves the UI at
<http://localhost:8888>. Pick a preset, press **Start Streaming**, then point the
ATLAS Stream Recorder at the broker with **Domain left empty**.

To run the pieces by hand instead:

```bash
docker compose up -d --wait
```

```bash
py -m pip install -r backend/requirements.txt
```

```bash
py -m uvicorn main:app --host 0.0.0.0 --port 8888 --app-dir backend
```

## Choosing channels

The UI lists every reading HWiNFO currently publishes, grouped by sensor and
showing live values, with a filter box. Presets are computed against your actual
sensor tree rather than a fixed list:

| Preset | Contents |
|---|---|
| `essential` | Curated summary — CPU/GPU load, temperature, power, clock, memory, fan |
| `cpu` / `gpu` / `memory` / `drives` / `network` | Everything under those sensors |
| `motherboard` | Anything not CPU, GPU, memory, drive or network |
| `temperatures` / `fans` / `power` / `clocks` / `voltages` / `usage` | By reading type |
| `full` | Every reading HWiNFO publishes |

ATLAS registers each parameter with its own gRPC round-trip, so session start
scales with channel count — the UI warns past 250. `full` on a well-instrumented
board can mean a noticeable wait before data starts flowing.

## Derived channels

Beyond what HWiNFO reports directly, the bridge can stream **calculated**
channels — a Fahrenheit conversion, a headroom margin below a throttle point,
a delta between two sensors, a threshold flag — computed each tick from other
channels' already-sampled values. No code required: edit
`configs/derived_channels.json`, e.g.

```json
{
  "metric_key": "CPU0_Tctl_F",
  "formula": "$CPU0_CPUTctlTdie * 1.8 + 32",
  "units": "F",
  "description": "CPU Tctl/Tdie in Fahrenheit",
  "min_value": 32,
  "max_value": 250,
  "format_string": "%5.1f"
}
```

`$Name` references another channel (real, or an earlier derived one).
Formulas are a restricted, whitelisted expression subset — arithmetic,
comparison, boolean logic, an `a if cond else b` conditional — validated at
load time so a formula can only combine numbers and `$`-references. See
[MANUAL.md §8](MANUAL.md#8-derived-channels) for the full syntax rules and how
this interacts with channel presets.

This is deliberately not the same thing as an ATLAS FDL Function — the
calculation runs **in the bridge**, before the value is ever sent, so it does
not depend on ATLAS at all. The result shows up in the bridge's own
`GET /api/status` → `current_values` and as a real Kafka packet on
`Default.Stream1`, so any downstream consumer gets the calculated value
without knowing the formula or running ATLAS — see
[MANUAL.md §8](MANUAL.md#8-derived-channels) for details.

## Sample rate

The default is 2 Hz, matching HWiNFO's own 2000 ms sensor polling period.
Sampling faster than HWiNFO polls just repeats values; lower **Settings →
Sensors → Sensor polling period** in HWiNFO first if you want more resolution.

The UI shows how long ago HWiNFO last refreshed the block and warns if that
stalls — the usual cause of a flat-lining trace.

## Tests

The shared-memory parsing is tested against a synthetic block, so HWiNFO does
not need to be running:

```bash
py backend/tests/test_hwinfo_reader.py
```

Covers both struct layouts, unit and naming derivation, preset selection,
duplicate labels, a missing section, and sensors being added mid-session.

Derived-channel formulas (see above) are tested the same way, against
synthetic config files:

```bash
py backend/tests/test_derived_channels.py
```

## Ports

| Service | Port |
|---|---|
| Bridge UI | 8888 |
| Kafka | 9092 |
| Kafka UI | 8080 |
| Stream API | 13579 |
| Key Generator | 15379 |

These are the ATLAS defaults, shared with sibling bridges in this family — only
one stack can be up at a time.

## Licence

MIT — see [LICENSE](LICENSE).
