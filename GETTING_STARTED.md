# Getting Started

Step-by-step setup, from nothing to a live trace in ATLAS.

## 1. Turn on HWiNFO's shared memory

The bridge reads HWiNFO's sensor block directly; without this setting there is
nothing to read.

1. Start **HWiNFO64**. Sensors-only mode is the right way to run it as a
   background source.
2. Open **Settings** (the gear icon) → **Main Settings**.
3. Tick **Shared Memory Support**.
4. Leave HWiNFO running.

To confirm it worked, once the bridge is up visit
<http://localhost:8888/api/hwinfo/status>. You should see `available: true` plus
sensor and reading counts.

> **Free version:** Shared Memory Support stops after 12 hours of HWiNFO
> runtime. The bridge will report stale data rather than fail — restart HWiNFO
> to resume. The Pro licence removes the limit.

## 2. Start Docker Desktop

Kafka, the Stream API and the Key Generator all run as containers. Docker
Desktop must be running before the next step.

## 3. Start the bridge

```bash
scripts\start.bat
```

This waits for the containers to report healthy, installs Python dependencies,
and serves the UI on <http://localhost:8888>.

If you would rather run it manually:

```bash
docker compose up -d --wait
```

```bash
py -m uvicorn main:app --host 0.0.0.0 --port 8888 --app-dir backend
```

## 4. Pick your channels

Open <http://localhost:8888>.

- Start with the **Essential** preset to check the path end to end.
- Switch to **Custom...** for the full sensor tree: filter by name, unit or
  reading type, and select whole sensors at a time.
- Keep an eye on the selected count. ATLAS registers every parameter with its
  own round-trip, so a few hundred channels means a slow session start.

## 5. Start streaming

Press **Start Streaming**. The status bar shows HWiNFO and Stream API
connectivity, the channel count, samples sent and elapsed time. Live values and
analysis appear below once data is flowing.

## 6. Connect ATLAS

1. Open **ATLAS 10**.
2. Open the **Stream Recorder**.
3. Point it at the Kafka broker on `localhost:9092`.
4. **Leave the Domain field empty** — it must match `AppConfig.json`, where
   `Domain` is an empty string.
5. The session appears with the name shown in the bridge UI.

## Troubleshooting

**"Could not read HWiNFO's shared memory"**
HWiNFO is not running, or Shared Memory Support is off — see step 1. If it was
working earlier and stopped, a free-version build has likely hit its 12-hour
limit; restart HWiNFO.

**"Failed to connect to Stream API. Is Docker running?"**
Docker Desktop is not running, or the containers have not finished starting.
Check with `docker compose ps` — all four should be up, with Kafka healthy.

**Session starts but no data appears in ATLAS**
Check the Domain field is empty in the Stream Recorder. Browse the Kafka topics
at <http://localhost:8080> to confirm packets are arriving on
`Default.Stream1`.

**Traces are flat or stepped**
The bridge is sampling faster than HWiNFO refreshes. Either lower the sample
rate or lower HWiNFO's **Settings → Sensors → Sensor polling period**.

**A sensor I want is missing**
The bridge only sees what HWiNFO publishes. If a reading is hidden in HWiNFO's
sensor window it will not appear here — unhide it there, then press **Rescan**
in the channel picker.

**Port already in use**
A sibling bridge stack is probably running on the same ATLAS default ports.
Stop it (`docker compose down` in that project) before starting this one.
