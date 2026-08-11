# ATLAS HWiNFO Kafka Stream — User Manual

Version 1.0.1

---

## Contents

1. [What this does](#1-what-this-does)
2. [Requirements](#2-requirements)
3. [Configuring HWiNFO](#3-configuring-hwinfo)
4. [Installation and first run](#4-installation-and-first-run)
5. [The bridge interface](#5-the-bridge-interface)
6. [Choosing channels](#6-choosing-channels)
7. [How channels appear in ATLAS](#7-how-channels-appear-in-atlas)
8. [Derived channels](#8-derived-channels)
9. [Connecting the ATLAS Stream Recorder](#9-connecting-the-atlas-stream-recorder)
10. [Sample rate and timing](#10-sample-rate-and-timing)
11. [The analysis panel](#11-the-analysis-panel)
12. [Configuration reference](#12-configuration-reference)
13. [HTTP API reference](#13-http-api-reference)
14. [Troubleshooting](#14-troubleshooting)
15. [How it works](#15-how-it-works)
16. [Running the tests](#16-running-the-tests)
17. [Known limits](#17-known-limits)

---

## 1. What this does

HWiNFO reads several hundred hardware sensors from your machine — per-core clocks
and temperatures, package and rail power, fan headers, drive S.M.A.R.T. values,
GPU hotspot deltas, memory timings, and explicit throttling flags. It displays
them, but it is not a telemetry analysis tool.

ATLAS *is* a telemetry analysis tool. This bridge connects the two, so hardware
sensors can be plotted, overlaid, zoomed and compared against each other on a
common time base — the same way you would analyse any other telemetry.

```
HWiNFO64
   │  shared memory (Global\HWiNFO_SENS_SM2)
   ▼
Python bridge  ── UI on http://localhost:8888
   │  gRPC
   ▼
Stream API (:13579)
   │
   ▼
Kafka (:9092)
   │
   ▼
ATLAS Stream Recorder
```

Typical uses: finding the thermal or power limit behind a frame-rate drop,
watching VRM temperature under sustained load, correlating fan response against
package power, or checking whether a cooler remount actually changed anything.

---

## 2. Requirements

| | |
|---|---|
| **OS** | Windows. HWiNFO's shared memory is a Windows section, opened here through `OpenFileMappingW`. |
| **HWiNFO64** | Running, with Shared Memory Support enabled. See §3. |
| **Docker Desktop** | Runs Kafka, the Stream API and the Key Generator. |
| **Python** | 3.10 or newer. Invoked as `py` (the Windows launcher). |
| **ATLAS 10** | With the Stream Recorder, to view the data. |

Verified against HWiNFO 8.24 and Python 3.14 on Windows 11.

---

## 3. Configuring HWiNFO

**This is the step that most often goes wrong, so do it first.**

1. Start **HWiNFO64**. When it offers a mode, **Sensors-only** is the right
   choice — it is the lightest way to run it as a background data source.
2. Open **Settings** (the gear icon).
3. On the **Main Settings** tab, tick **Shared Memory Support**.
4. Leave HWiNFO running. The bridge reads from it continuously; closing HWiNFO
   stops the data.

### Verifying it worked

With the bridge running, open <http://localhost:8888/api/hwinfo/status>. A
healthy response looks like:

```json
{
  "available": true,
  "version": 2,
  "revision": 1,
  "sensor_count": 17,
  "reading_count": 329,
  "poll_age_seconds": 0.88
}
```

`available: false` means the setting is off or HWiNFO is not running.

### The 12-hour limit on free HWiNFO

On the **free** version, Shared Memory Support switches itself off after
12 hours of HWiNFO runtime. The bridge does not crash when this happens — it
keeps the ATLAS session alive and reports stale data — but values stop changing.
Restart HWiNFO to restore it. The Pro licence removes the limit.

The interface warns you when HWiNFO has not refreshed for more than 30 seconds,
which is the usual sign this has happened.

### Sensor visibility

The bridge only sees what HWiNFO publishes. If you have hidden a reading in
HWiNFO's own sensor window, it will not appear here. Unhide it in HWiNFO, then
press **Rescan** in the channel picker.

---

## 4. Installation and first run

### The simple path

```bash
scripts\start.bat
```

This starts the Docker containers, waits for them to report healthy, installs the
Python dependencies, and serves the interface at <http://localhost:8888>.

Press `Ctrl+C` to stop; the script shuts the containers down on the way out.

### Running the parts by hand

Start the supporting services:

```bash
docker compose up -d --wait
```

Install dependencies (once):

```bash
py -m pip install -r backend/requirements.txt
```

Run the server:

```bash
py -m uvicorn main:app --host 0.0.0.0 --port 8888 --app-dir backend
```

Check the containers are healthy at any time:

```bash
docker compose ps
```

---

## 5. The bridge interface

Open <http://localhost:8888>.

### Status bar

| Indicator | Meaning |
|---|---|
| **HWiNFO** | Green once the shared memory section has been opened. |
| **Stream API** | Green once the gRPC connection to the Stream API succeeds. |
| **Streaming** | Green while a session is active. |
| **channels** | How many channels this session registered. |
| **samples** | Running total of samples sent since the session started. |
| **elapsed** | Time since the session started. |

### Configuration

- **Session Name** — optional. Left blank, it becomes
  `<hostname> HWiNFO - <date> <time>`. This is the name the session appears
  under in ATLAS, so a descriptive name is worth setting if you are comparing
  runs later.
- **Channel Preset** — a curated selection, with the channel count shown in
  brackets. Choose **Custom...** to pick individual readings.

### Controls

**Start Streaming** creates the ATLAS session and begins sending. It is disabled
while HWiNFO is unavailable.

Starting is not instant. ATLAS registers each parameter with its own round-trip,
so the button shows *Starting...* until every channel is registered — a few
seconds for a preset, considerably longer for `full`.

**Stop Streaming** ends the session cleanly and closes it in ATLAS.

---

## 6. Choosing channels

### Presets

Presets are evaluated against the sensors your machine actually reports, not a
fixed list, so counts vary by hardware. The figures below are from a
Ryzen 9 7900X3D / Radeon / MSI MAG B650 system reporting 329 readings.

| Preset | Contents | Example count |
|---|---|---|
| `essential` | Curated summary — CPU/GPU load, temperature, power, clock, memory, fan | 12 |
| `cpu` | Everything under the CPU sensors | 214 |
| `gpu` | Everything under the GPU sensors | 24 |
| `memory` | System and video memory, wherever reported | 14 |
| `drives` | Drive temperatures, activity, S.M.A.R.T. | 14 |
| `network` | Network adapter sensors | 8 |
| `motherboard` | Mainboard sensors, plus anything uncategorised | 69 |
| `temperatures` | All temperature readings | 34 |
| `fans` | All fan readings | 3 |
| `power` | All power readings | 22 |
| `clocks` | All clock readings | 49 |
| `voltages` | All voltage readings | 37 |
| `usage` | All usage/load readings | 105 |
| `full` | Everything HWiNFO publishes | 329 |

**Start with `essential`** to confirm the whole path works before committing to
a large channel set.

`essential` fills twelve slots where the hardware provides them: CPU usage,
temperature, package power and clock; GPU load, temperature, power, clock and
memory; physical and virtual memory; and the CPU fan. Vendors name these
differently — AMD reports *GPU ASIC Power* where NVIDIA reports *GPU Power*, and
MSI labels its CPU fan header simply *CPU* — and the preset accounts for the
common variants.

### The custom picker

Choosing **Custom...** opens the full sensor tree, grouped by HWiNFO sensor with
current values shown alongside each reading.

- **Filter box** — matches sensor name, label, unit and reading type. Typing
  `fan` narrows to fan headers across every sensor; `°C` is written `C`.
- **Group headers** — click to collapse. `all` / `none` select within one sensor.
- **Select Filtered** — selects everything currently visible, which combined with
  the filter is the fastest way to grab, say, every power reading on the CPU.
- **Rescan** — re-reads HWiNFO. Use after unhiding sensors in HWiNFO, or when
  hardware has woken up.

### Watch the channel count

ATLAS registers every parameter with its own gRPC round-trip, so **session start
time scales with the number of channels**. The interface warns past 250. A few
hundred channels means a noticeable wait before data begins flowing; this is
inherent to the registration model, not a fault.

Streaming rate is unaffected — only session start is slower.

---

## 7. How channels appear in ATLAS

### Naming

Channel keys are built as `SensorSlug_LabelSlug`:

| HWiNFO sensor | HWiNFO label | ATLAS channel |
|---|---|---|
| `CPU [#0]: AMD Ryzen 9 7900X3D` | `Total CPU Usage` | `CPU0_TotalCPUUsage` |
| `CPU [#0]: AMD Ryzen 9 7900X3D` | `CPU (Tctl/Tdie)` | `CPU0_CPUTctlTdie` |
| `GPU [#0]: AMD Radeon` | `GPU ASIC Power` | `GPU0_GPUASICPower` |
| `System: MSI MS-7D75` | `Physical Memory Used` | `System_PhysicalMemoryUsed` |

The full ATLAS parameter identifier is `<channel>:HWiNFO`.

Where a board labels two different readings identically — MSI reports both a
temperature and a fan header as `CPU` — the second is qualified by reading type,
giving `..._CPU` and `..._CPU_Fan`. Identical labels of the *same* type get a
numeric suffix instead: `..._Fan`, `..._Fan_2`.

### Units

Units come from HWiNFO, normalised to ASCII because ATLAS parameter units are
plain strings: `°C` becomes `C`, `°F` becomes `F`. `RPM`, `W`, `V`, `MHz`, `%`,
`MB`, `Yes/No` and the rest pass through unchanged.

### Yes/No readings

HWiNFO reports throttling and warning flags as `Yes/No`, which arrive in ATLAS as
**0 or 1** with a range of 0–1. These are among the most useful channels it
offers — *Thermal Throttling (HTC)*, *PROCHOT*, *Throttle Reason - Power*,
*PMIC Over Voltage*, *Drive Failure* — because they state a limit outright
rather than leaving it to be inferred from a clock dropping.

### Grouping

Everything lands in a single ATLAS group named `HWiNFO`. This is deliberate and
not adjustable: ATLAS silently discards a configuration packet carrying more than
one group definition. The per-sensor grouping you see in the picker is a feature
of the bridge interface only.

### Ranges

Minimum and maximum are derived from the unit where it is informative, otherwise
from the reading type — temperatures 0–120, fans 0–8000 RPM, voltages 0–24,
usage 0–100, and so on. These set the default axis scaling in ATLAS; adjust
there if a channel needs a tighter range.

---

## 8. Derived channels

Beyond what HWiNFO reports directly, the bridge can stream **calculated**
channels — values computed from other channels' already-sampled readings each
tick, rather than read from HWiNFO. A Fahrenheit conversion, a headroom margin
below a throttle point, a delta between two related sensors, a 0/1 flag for
"is this over threshold" — these ride the same `ConfigurationPacket` /
`PeriodicDataPacket` machinery as every other channel, so they are real
recorded channels in ATLAS, not something computed after the fact.

### Adding one

Edit `configs/derived_channels.json` — no code changes needed. Each entry:

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

- `$Name` in a formula references another channel's `metric_key` — a real one,
  or an earlier entry in the same file (derived channels can chain).
- Formulas are arithmetic, comparison, boolean (`and`/`or`/`not`) and a
  conditional (`a if cond else b`), written as Python expression syntax after
  substituting `$Name` → `Name`. `**` is power, not FDL's `^`. Every formula is
  checked against a strict whitelist when the bridge starts — no function
  calls, attribute access, subscripting or lambdas — so a formula can only
  combine numbers and `$`-references with operators.
- `units`, `description`, `min_value`, `max_value` and `format_string` behave
  exactly as they do for a real channel — they set the ATLAS parameter
  definition and default axis scaling.

### When a derived channel activates

A derived channel needs every `$`-reference it uses to be part of **the
current session's selected channels** — not just present somewhere on the
machine. Picking the `essential` preset when a formula references a channel
only present in `full` means that derived channel is silently skipped for
this session, the same way an empty preset category is skipped. Switch to a
preset (or custom selection) that includes the channels a formula depends on,
or use `full`, if you want it to activate.

A missing reference is never an error — check `GET /api/channels` (§13) for
the exact live `metric_key` names on your machine before writing a formula
against them, since naming depends on your CPU/GPU/board and how HWiNFO
labels each reading.

---

## 9. Connecting the ATLAS Stream Recorder

1. Open **ATLAS 10**.
2. Open the **Stream Recorder**.
3. Point it at the Kafka broker on `localhost:9092`.
4. **Leave the Domain field empty.** It must match `configs/AppConfig.json`,
   where `Domain` is an empty string. A mismatch here is the most common reason
   a session never appears.
5. The session appears under the name shown in the bridge interface.

Kafka topics follow `<Domain>.<DataSource>.<Stream>`, so with an empty domain the
data stream is `Default.Stream1`. You can browse it at <http://localhost:8080> to
confirm packets are arriving.

---

## 10. Sample rate and timing

The default is **2 Hz**, matching HWiNFO's default 2000 ms sensor polling period.

**Sampling faster than HWiNFO polls does not give more resolution** — it repeats
the same value. To genuinely sample faster, lower HWiNFO's own period first:
**Settings → Sensors → Sensor polling period**. Then raise the bridge rate (see
§12). Be aware that a low HWiNFO polling period increases its own CPU use and,
on some boards, contends with the Super-I/O chip.

Timestamps are contiguous by construction: each batch starts exactly where the
previous one ended, rather than being re-read from the clock. This keeps traces
continuous in ATLAS regardless of scheduling jitter on the sampling loop.

The interface shows how long ago HWiNFO last refreshed its block, and warns past
30 seconds — the usual sign that HWiNFO has stopped publishing.

---

## 11. The analysis panel

While streaming, plain-English findings appear above the live values. They come
from two sources.

**HWiNFO's own flags**, which are statements of fact rather than inferences:

| Finding | Trigger |
|---|---|
| Thermal throttling active | Any `Thermal Throttling` flag reading Yes |
| Power limit reached | `Power Limit Exceeded`, `PPT Limit`, package power limit |
| Current limit reached | `TDC` / `EDC` limit flags |
| GPU capped by temperature / power | `PerfCap Reason` / `Throttle Reason` flags |
| Critical temperature reported | Any `Critical Temperature` flag |

**Threshold checks**, for what HWiNFO does not state outright:

| Finding | Threshold |
|---|---|
| CPU running hot | ≥ 95 °C (warning from 90 °C) |
| GPU temperature climbing | ≥ 83 °C |
| Large GPU hotspot delta | hotspot exceeds GPU temperature by ≥ 20 °C — worth checking mounting pressure or paste |
| CPU-bound / GPU-bound | one processor ≥ 90% while the other is ≤ 40% |
| Memory pressure | ≥ 90% used |
| Fan stopped while hot | a fan reads 0 RPM while any temperature is ≥ 60 °C |

These are guidance for spotting a pattern quickly, not a substitute for reading
the traces.

---

## 12. Configuration reference

### Bridge settings — `backend/config.py`

| Setting | Default | Notes |
|---|---|---|
| `stream_api_address` | `localhost:13579` | gRPC endpoint for all data writes |
| `key_generator_address` | `localhost:15379` | Supplies unique session and config IDs |
| `data_source` | `Default` | First element of the Kafka topic name |
| `stream` | `Stream1` | Data stream name |
| `sample_frequency_hz` | `2` | See §10 before raising |
| `default_preset` | `essential` | |

Several of these can be changed at runtime via `PUT /api/config` (§13) without
editing the file. `sample_frequency_hz` is clamped to 1–20.

### Stream API — `configs/AppConfig.json`

`Domain` is an empty string, and must stay in step with the Stream Recorder's
Domain field. `StreamCreationStrategy` is `TopicBased`. The broker URL is the
in-Docker address `kafka:9094`, which is correct — it is how the Stream API
container reaches Kafka, not how your machine does.

### Ports

| Service | Port |
|---|---|
| Bridge UI | 8888 |
| Kafka (external) | 9092 |
| Kafka (internal to Docker) | 9094 |
| Kafka UI | 8080 |
| Stream API | 13579 |
| Stream API metrics | 10010 |
| Key Generator | 15379 |

These are the ATLAS defaults and are shared with sibling bridges in this family,
so **only one such stack can run at a time**.

---

## 13. HTTP API reference

All endpoints are under `/api` on port 8888. The interface uses these, and they
are equally usable for scripting.

### `GET /api/hwinfo/status`

Whether the shared memory section can be read, with block metadata.

```json
{ "available": true, "version": 2, "revision": 1,
  "sensor_count": 17, "reading_count": 329, "poll_age_seconds": 0.88 }
```

### `GET /api/channels`

Discovers what HWiNFO is publishing right now — every channel with its current
value, plus each preset and how many channels it would select. Discovery runs per
request rather than being cached, so it reflects sensors coming and going.

### `GET /api/status`

Live bridge state: connection flags, session key, channel count, samples sent,
elapsed time, current values, analysis findings, HWiNFO poll age, and the last
error if any.

### `POST /api/start`

```json
{ "preset": "essential", "session_name": "Optional name" }
```

or an explicit selection:

```json
{ "preset": null, "custom_channels": ["CPU0_TotalCPUUsage", "GPU0_GPUTemperature"] }
```

Returns immediately — the session is created on a background thread. Poll
`/api/status` to see whether it succeeded; failures surface in `error`.

### `POST /api/stop`

Ends the session and stops streaming.

### `GET /api/config` · `PUT /api/config`

Read or update `stream_api_address`, `data_source`, `stream`, `default_preset`
and `sample_frequency_hz`. Changes apply to the next session.

---

## 14. Troubleshooting

### "Could not read HWiNFO's shared memory"

HWiNFO is not running, or Shared Memory Support is off — see §3. If it worked
earlier and has stopped, a free-version install has probably hit its 12-hour
limit; restart HWiNFO.

### "Failed to connect to Stream API. Is Docker running?"

Docker Desktop is not running, or the containers have not finished starting. Run
`docker compose ps` — all four services should be up, with Kafka healthy.

### Session starts, but nothing appears in ATLAS

Check the **Domain field is empty** in the Stream Recorder (§9). Then open the
Kafka UI at <http://localhost:8080> and confirm packets are arriving on
`Default.Stream1`. If they are, the problem is on the ATLAS side; if not, check
the bridge log.

### Every channel reads zero

Fixed in **v1.0.1**. HWiNFO 8.x publishes a larger shared-memory block than the
classic documented layout, and v1.0.0 read the values from four bytes past where
they live — which yielded correctly named channels carrying flat zeroes.

If you are on v1.0.1 or later and still see this, check the bridge log at
startup for the detected layout:

```
HWiNFO reading layout: 316-byte prefix in a 460-byte row (64/64 sample values plausible)
```

A low plausible count there means the block does not match either known layout —
worth reporting, with your HWiNFO version.

Note that some channels read zero quite legitimately: throttle flags reading No,
an unused network adapter, idle GPU compute engines. Check the reading in
HWiNFO itself before assuming a fault.

### Traces are flat or stepped

The bridge is sampling faster than HWiNFO refreshes. Lower the sample rate, or
lower HWiNFO's polling period — see §10.

### Values stop updating mid-session

Check the HWiNFO poll age in the interface. A climbing figure means HWiNFO has
stopped publishing: either it was closed, or the free version's 12-hour limit
expired. Restart HWiNFO. The bridge reconnects on its own; the ATLAS session
survives.

### A sensor I want is missing

The bridge only sees what HWiNFO publishes. Unhide the reading in HWiNFO's
sensor window, then press **Rescan**.

### Session start is very slow

Expected with a large channel set — one gRPC round-trip per parameter (§6). Use
a smaller preset if start time matters.

### "Port already in use"

Another bridge stack from this family is running on the same ATLAS default ports.
Run `docker compose down` in that project first.

### Channels are missing after a sensor appeared mid-session

The ATLAS configuration packet is sent once at session start and never resent, so
the channel set is fixed for the life of a session. Restart the session to pick
up new sensors.

---

## 15. How it works

### Reading HWiNFO

HWiNFO publishes a shared-memory section containing two tables: **sensors** (the
hardware sources) and **readings** (individual values, each pointing back at its
sensor by row index).

The section is opened with `OpenFileMappingW`, never `mmap`. On Windows, Python's
`mmap` with a tagname goes through `CreateFileMapping`, which *creates* the
section when it is absent — so a missing HWiNFO would yield a block of zeroes
instead of an error, and could occupy the name HWiNFO wants at its next start.

**Row indices are not stable.** HWiNFO renumbers rows whenever sensors come and
go — a drive spinning up, a GPU leaving idle. Channels are therefore keyed by the
`(sensor id, sensor instance, reading id)` triple, which survives that. Each
sample verifies the cached row still holds the expected reading and re-scans if
not, so a channel can never silently start reporting a different sensor.

**The block layout is detected, not assumed.** HWiNFO 8.x publishes a "v2" block
with larger rows than the classic documentation describes (460-byte readings,
392-byte sensors) because a UTF-8 copy of each string is appended after the
existing fields. Since labels sit *before* the values, a wrongly chosen layout
produces perfectly named channels carrying garbage — so the header is validated
against a structural invariant, and the row format is chosen by checking that the
values actually decode to plausible numbers.

### Writing to ATLAS

Packets go through the gRPC Stream API, never directly to Kafka — writing
straight to Kafka bypasses session and format registration, and ATLAS would never
see the data.

The sequence at session start is fixed: create the session, send a new-session
packet to both streams, pause for registration, send the configuration packet to
both streams, then register a data format ID per parameter. During streaming,
each parameter gets its own periodic data packet. Sends happen on a single
background worker so packet order is preserved while the sampling loop stays on
schedule.

The engine keeps a running timestamp rather than re-reading the clock per batch,
so consecutive batches are exactly contiguous.

For the full set of hard-won constraints, see `CLAUDE.md` in the repository root.

---

## 16. Running the tests

The shared-memory parsing and engine timing are tested against synthetic blocks,
so HWiNFO does not need to be running:

```bash
py backend/tests/test_hwinfo_reader.py
```

```bash
py backend/tests/test_bridge_engine.py
```

Between them these cover all three known block layouts, header selection, channel
naming and unit normalisation, preset selection, duplicate labels, sensors
appearing mid-session, a missing section, batch contiguity and the sample counter.

Derived-channel formulas (§8) are tested the same way, against synthetic config
files rather than the shipped `configs/derived_channels.json`:

```bash
py backend/tests/test_derived_channels.py
```

Covers formula compilation, the AST safety whitelist rejecting calls/attribute
access/comprehensions/lambdas, evaluation, missing-reference handling, and
chaining one derived channel onto another.

All three files are pytest-compatible and also run standalone as above.

---

## 17. Known limits

- **Windows only.** The shared-memory interface is Windows-specific.
- **The channel set is fixed per session.** ATLAS receives one configuration
  packet at session start; sensors appearing later need a new session.
- **One ATLAS group.** ATLAS silently rejects multiple group definitions, so all
  channels share the `HWiNFO` group.
- **Session start scales with channel count**, at one round-trip per parameter.
- **Resolution is bounded by HWiNFO's polling period**, not by this bridge.
- **Free HWiNFO stops publishing after 12 hours** of runtime.
- **Only one bridge stack at a time**, since ports are shared across the family.
- **No historical backfill.** Streaming begins when you press Start; HWiNFO's own
  min/max/average history is not sent.
- **Derived channels need their references in the same session's selection**
  (§8) — not just present on the machine — and count toward the per-parameter
  registration round-trips like any other channel.
