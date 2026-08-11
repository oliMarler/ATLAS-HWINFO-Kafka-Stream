# HWiNFO ATLAS Bridge

## Project Goal
Stream live hardware sensor data from [HWiNFO](https://www.hwinfo.com/) into Motion Applied ATLAS using the MA Data Platforms Streaming Support Library. Readings are pulled from HWiNFO's shared-memory sensor block and written to ATLAS via the Stream API's gRPC services.

## Architecture
```
HWiNFO64 (Global\HWiNFO_SENS_SM2) → Python Bridge → gRPC Stream API (:13579) → Kafka (:9092) → ATLAS Stream Recorder
```

- **No direct Kafka writes.** All data goes through the gRPC Stream API. Writing directly to Kafka bypasses session/format registration and ATLAS will never see the data.
- **Key Generator** service at `:15379` provides unique IDs for sessions and config packets.
- **Kafka UI** at `:8080` for debugging topic contents.
- **Docker Compose** runs Kafka (KRaft mode, no ZooKeeper), Stream API, and Key Generator.
- **Channels are built at bridge-start time, not import time.** The sensor set depends on the machine, the board's Super-I/O chip, which drives are awake, and what the user has hidden in HWiNFO's own UI — none of which is known when the server boots. `channel_registry.build_channels()` is called from `bridge_engine.py` right after `HwinfoReader.connect()`.
- **Presets are predicates, not key lists.** "All temperatures" has to mean whatever this machine reports, so `PRESET_BUILDERS` holds functions over the discovered `ChannelDef` list.

## Documentation Links
- HWiNFO shared memory: documented in the HWiNFO SDK (`HWiNFO Manual.pdf`, shipped in the install directory)
- Support Library Sample Usage: https://github.com/mat-docs/MA.DataPlatforms.Streaming.Support.Library.SampleUsage/tree/main
- ATLAS Reference Docs: https://atlas.motionapplied.com/developer-resources/secu4/support_library/reference_docs/
- ATLAS API Reference: https://atlas.motionapplied.com/developer-resources/secu4/support_library/reference_docs/api-reference/
- ATLAS Stream API Getting Started: https://atlas.motionapplied.com/developer-resources/secu4/stream_api/reference_docs/getting-started/overview/

## Critical Rules (Hard-Won Lessons)

Rules 1–8 govern the gRPC/Kafka mechanics and apply regardless of what data is being streamed. Rules 9–13 are specific to HWiNFO as a source.

### 1. Packet Send Order Matters
Must be exactly:
1. `CreateSession` (gRPC call)
2. `NewSessionPacket` → both main stream (`""`) and data stream (`"Stream1"`)
3. `sleep(1)` — give Stream API time to register the session
4. `ConfigurationPacket` → **both** main stream (`""`) and data stream (`"Stream1"`), `is_essential=True`
5. `GetParameterDataFormatId` (gRPC call, one per parameter)
6. `PeriodicDataPacket` → data stream
7. `EndOfSessionPacket` → both streams, then `EndSession` gRPC call

### 2. One Parameter Per Packet
- Register a **separate data format ID per parameter** via `GetParameterDataFormatId` with a single-element `parameters` list.
- Send a **separate `PeriodicDataPacket` per parameter**, each with its own `data_format_identifier` and exactly 1 `SampleColumn`.
- Do NOT bundle multiple parameters into one packet with one shared format ID.
- **Scaling note:** HWiNFO commonly publishes 300–800 readings. The `full` preset therefore means that many sequential `GetParameterDataFormatId` round trips at session start. That is inherent to the per-parameter registration model, not a bug — the UI warns above `CHANNEL_COUNT_WARNING` (250).

### 3. Single GroupDefinition Only
ATLAS **silently rejects** a `ConfigurationPacket` with multiple `GroupDefinition` entries. No error, no log, just nothing happens. Always use exactly one group, however many sensors exist:
```python
group_defs = [
    open_data_pb2.GroupDefinition(
        identifier="HWiNFO",
        application_name="HWiNFO",
        name="HWiNFO",
        description="Hardware sensor readings from HWiNFO",
    )
]
```
`channel_registry.get_groups()` and `ChannelDef.group` exist for the **UI picker only** and never reach the config packet.

### 4. Contiguous Timestamps
Each batch's `start_time` must equal the previous batch's end time (`previous_start + interval * sample_count`). Gaps cause discontinuous traces in ATLAS. `bridge_engine.py` seeds `_next_timestamp_ns` from the wall clock once at session start and advances it by `interval_ns * count` per batch — it does **not** re-read the clock per batch, so loop jitter cannot open a gap.

### 5. All Timestamps in Nanoseconds
`start_time`, `interval`, and marker `timestamp` are all in nanoseconds. `interval_ns = int(1e9 / frequency_hz)`.

### 6. Config Packet Is Not Resent
The Configuration packet is sent once at session start. Do not resend it periodically. If ATLAS misses it (e.g. Stream Recorder reconnects), start a new session. This also means the channel set is fixed for the life of a session — a sensor appearing mid-session does not add a channel.

### 7. ConfigurationPacket Must Go to Both Streams
SQLRace requires the `ConfigurationPacket` on every stream it needs to write to. Without it, packets on that stream are silently ignored. Send config to both main stream (`""`) and data stream (`"Stream1"`).

### 8. Use KeyGenerator for config_id
Generate `config_id` via the KeyGenerator gRPC service, not a hardcoded string.

### 9. Open the Shared Memory, Never Create It
Do **not** reach for `mmap.mmap(-1, size, tagname=...)`. On Windows that goes through `CreateFileMapping`, which *creates* the section when it is absent — so a missing HWiNFO yields a block of zeroes instead of an error, and our process could squat on the name HWiNFO wants at its next start. It also rejects a zero length against an anonymous handle, so the size cannot be discovered that way. `shared_memory.py` uses `OpenFileMappingW` + `MapViewOfFile` via ctypes, which fails cleanly when the section does not exist.

### 10. Reading Row Indices Are Not Stable
HWiNFO renumbers rows whenever sensors come and go — a drive spinning up, a GPU leaving idle. Never key a channel by its row index. Channels are keyed by the `(dwSensorID, dwSensorInst, dwReadingID)` triple; `hwinfo_reader._sample_rows()` verifies the cached row still holds the expected reading on every sample and forces a re-scan when it does not.

### 11. The Struct Layout Is Detected, Never Assumed — Getting It Wrong Fails Silently
**HWiNFO packs these structs. There is no alignment padding**, despite what a natural reading of the published C implies. Verified against HWiNFO 8.24 on the dev machine.

HWiNFO 8.x publishes a **"v2" block** (`dwVersion=2`) with larger rows than the classic documentation describes, because a UTF-8 copy of each string is appended *after* the existing fields:

| | classic | v2 (HWiNFO 8.x) | layout |
|---|---|---|---|
| header | 44 | 44 | `<IIIqIIIIII` |
| sensor row | 264 | **392** | `<II128s128s` + UTF-8 `128s` |
| reading row | 316 | **460** | `<III128s128s16sdddd` + UTF-8 `128s16s` |

Within a v2 reading row: label at 12 and 140, unit at 268, and **value/min/max/avg at 284/292/300/308**.

**Why this needs detecting rather than assuming:** the labels sit *before* the values. Pick the wrong layout and every channel still gets a perfect name, correct units and a healthy-looking config packet — while every value decodes from four bytes off, landing on a denormal that formats as `0.0`. Nothing raises. This shipped in v1.0.0 and produced a full set of flat-zero traces in ATLAS.

Two checks guard it, both in `hwinfo_reader.py`:
- **Header** — candidates must satisfy `sensor_offset + sensor_element_size * sensor_count == reading_offset`. The tables are adjacent, so a layout guessed wrong shifts every field by one and fails this. The looser range checks alone are *not* enough; they let the wrong parse through on some machines.
- **Rows** — `_detect_reading_layout()` decodes a sample of rows with each candidate and scores the values. **Zeros must score nothing**: reading a padded row at the unpadded offset returns padding plus the low half of the value, which is all-zero for most readings and would otherwise look like a flawless decode. Score non-zero plausible values, penalise NaN/denormals.

Rows are always walked using the element size the header reports, so a future HWiNFO that appends further fields still reads correctly. `backend/tests/test_hwinfo_reader.py` covers all three layouts against synthetic blocks, so HWiNFO need not be running to test parsing.

### 12. HWiNFO's Poll Period Caps the Useful Sample Rate
HWiNFO refreshes its sensors every 2000 ms by default, so sampling faster than 2 Hz just repeats values. Lower HWiNFO's own period (Settings > Sensors > Sensor polling period) before raising `sample_frequency_hz`. `HwinfoReader.poll_age_seconds()` exposes the staleness — the UI warns when it climbs past 30 s, which usually means HWiNFO stopped publishing.

### 13. Shared Memory Support Is a Prerequisite, and Expires on Free Builds
`Settings > Main Settings > Shared Memory Support` must be ticked, and HWiNFO must be running (Sensors-only mode is fine). On the **free** version this feature stops after 12 hours of runtime and needs an HWiNFO restart; the Pro licence removes the limit. Losing the section mid-session is handled gracefully — samples read as `None` (sent as `0.0`) and the reader retries — it does not tear down the ATLAS session.

## Derived Channels
Additional ATLAS parameters computed from other channels' values, rather than read from HWiNFO directly — e.g. a Fahrenheit conversion or a headroom calculation over a temperature channel. Defined in `configs/derived_channels.json`, no Python required to add one:
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
- `$Name` references another channel's `metric_key` (real or, if listed earlier in the file, another derived channel).
- Formulas are parsed as **Python expressions** after substituting `$Name` → `Name` — arithmetic, comparison, boolean (`and`/`or`/`not`), and a conditional (`a if cond else b`) are supported, `**` for power. This is inspired by ATLAS's own FDL function syntax but is not FDL: only the single-expression subset applies, since a derived channel is one scalar per sample, not a multi-statement function with loops.
- Every formula is validated against an AST whitelist at load time — no calls, attribute access, subscripting, comprehensions or lambdas — so a formula can only combine numbers and `$`-references with operators.
- A derived channel whose `$`-references aren't in the session's resolved channel set is skipped silently (e.g. no CPU temp sensor on this machine), same as the built-in presets when a category is empty.
- Computed once per sample tick in `bridge_engine.py`, from that tick's already-sampled real values — no extra HWiNFO reads, no separate timing path. It rides the same `ConfigurationPacket`/`PeriodicDataPacket` machinery as every other channel, so it's a real recorded channel, not a display-time calculation.

## Key Files
- `backend/bridge/shared_memory.py` — `OpenFileMappingW`/`MapViewOfFile` wrapper for read-only access to an existing named section
- `backend/bridge/hwinfo_reader.py` — parses HWiNFO's sensor/reading tables, stable-triple keying, fast per-sample row reads, reconnect handling
- `backend/bridge/channel_registry.py` — `ChannelDef`, `build_channels()`, naming/unit/range derivation, preset predicates
- `backend/bridge/derived_channels.py` — formula compiler/evaluator for `configs/derived_channels.json` (see Derived Channels above)
- `backend/bridge/atlas_writer.py` — gRPC client to Stream API (session lifecycle, config, data) — reused as-is across bridge variants apart from the group literal
- `backend/bridge/bridge_engine.py` — orchestrates reader → writer, discovers channels post-connect, batching and contiguous timing
- `backend/bridge/analysis.py` — findings from HWiNFO's own throttle/limit flags plus threshold checks
- `backend/api/routes.py` — FastAPI endpoints: start/stop/status/config, live `/channels` discovery, `/hwinfo/status`
- `backend/tests/test_hwinfo_reader.py` — synthetic shared-memory tests, runnable with `py backend/tests/test_hwinfo_reader.py`
- `backend/tests/test_derived_channels.py` — formula compiler/evaluator tests, runnable with `py backend/tests/test_derived_channels.py`
- `configs/AppConfig.json` — Stream API configuration (broker URL, domain, partitions)
- `configs/derived_channels.json` — derived channel formulas, hand-edited to add new calculations
- `docker-compose.yml` — Kafka, Stream API, Key Generator, Kafka UI
- `scripts/start.bat` — Windows startup script (Docker + backend)

## Services & Ports
| Service | Port | Purpose |
|---------|------|---------|
| Kafka | 9092 | Message broker (external) |
| Kafka | 9094 | Message broker (internal/docker) |
| Stream API | 13579 | gRPC endpoint for all data writes |
| Key Generator | 15379 | Unique ID generation |
| Kafka UI | 8080 | Web UI for browsing topics |
| Bridge UI | 8888 | FastAPI backend + frontend |

These are the ATLAS defaults and are shared with the sibling bridges in this family, so only one stack can be up at a time.

## AppConfig
- `StreamCreationStrategy`: `TopicBased`
- `Domain`: empty string (leave Domain empty in ATLAS Stream Recorder)
- Kafka topics follow pattern: `<Domain>.<DataSource>.<Stream>` (e.g. `Default.Stream1`)

## Windows Python Environment
The user has multiple Python installations. `python.exe` may not be on PATH. Always use `py` (the Windows launcher) in scripts:
```bat
py -m pip install -r requirements.txt
py -m uvicorn main:app --host 0.0.0.0 --port 8888
```

## Git Conventions
- Do NOT add `Co-Authored-By` trailers to commits.
- Push to feature branches, not master, unless explicitly asked.
