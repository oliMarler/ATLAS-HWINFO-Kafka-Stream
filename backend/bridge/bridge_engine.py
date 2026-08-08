import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime

from bridge.analysis import analyze
from bridge.atlas_writer import AtlasWriter
from bridge.channel_registry import ChannelDef, build_channels, resolve_channels
from bridge.derived_channels import evaluate as evaluate_derived
from bridge.derived_channels import load_specs as load_derived_specs
from bridge.derived_channels import resolve as resolve_derived
from bridge.hwinfo_reader import HwinfoReader, HwinfoUnavailable
from bridge.sample_value import SampleValue
from config import BridgeConfig

logger = logging.getLogger(__name__)


@dataclass
class BridgeStatus:
    source_connected: bool = False
    atlas_connected: bool = False
    streaming_active: bool = False
    session_key: str | None = None
    samples_sent: int = 0
    elapsed_seconds: float = 0.0
    active_channels: list[str] = field(default_factory=list)
    error: str | None = None
    current_values: dict[str, float] = field(default_factory=dict)
    insights: list[dict[str, str]] = field(default_factory=list)
    channel_count: int = 0
    hwinfo_poll_age_seconds: float | None = None


class BridgeEngine:
    def __init__(self, config: BridgeConfig) -> None:
        self._config = config
        self._status = BridgeStatus()
        self._lock = threading.Lock()
        self._running = False
        self._thread: threading.Thread | None = None
        self._channels: list[ChannelDef] = []
        self._next_timestamp_ns: int = 0
        self._start_time: float = 0.0

    def is_running(self) -> bool:
        with self._lock:
            return self._running

    def get_status(self) -> BridgeStatus:
        with self._lock:
            return BridgeStatus(
                source_connected=self._status.source_connected,
                atlas_connected=self._status.atlas_connected,
                streaming_active=self._status.streaming_active,
                session_key=self._status.session_key,
                samples_sent=self._status.samples_sent,
                elapsed_seconds=self._status.elapsed_seconds,
                active_channels=list(self._status.active_channels),
                error=self._status.error,
                current_values=dict(self._status.current_values),
                insights=list(self._status.insights),
                channel_count=self._status.channel_count,
                hwinfo_poll_age_seconds=self._status.hwinfo_poll_age_seconds,
            )

    def start(
        self,
        preset: str | None = None,
        custom_channels: list[str] | None = None,
        stream_api_address: str | None = None,
        key_generator_address: str | None = None,
        session_name: str | None = None,
    ) -> tuple[bool, str]:
        """Start streaming.

        Channels are named rather than resolved by the caller: the set that
        exists is only known once HWiNFO's shared memory has been read, which
        happens on the worker thread after both connections are up.
        """
        with self._lock:
            if self._running:
                return False, "Bridge is already running"
            self._running = True
            self._status = BridgeStatus(streaming_active=True)

        self._thread = threading.Thread(
            target=self._run,
            args=(
                preset,
                custom_channels,
                stream_api_address or self._config.stream_api_address,
                key_generator_address or self._config.key_generator_address,
                session_name,
            ),
            daemon=True,
        )
        self._thread.start()
        return True, "Bridge started"

    def stop(self) -> tuple[bool, str]:
        with self._lock:
            if not self._running:
                return False, "Bridge is not running"
            self._running = False
        if self._thread:
            self._thread.join(timeout=15)
            self._thread = None

        with self._lock:
            self._status.streaming_active = False

        return True, "Bridge stopped"

    def _fail(self, message: str) -> None:
        logger.error("%s", message)
        with self._lock:
            self._status.error = message
            self._status.streaming_active = False
        self._running = False

    def _run(
        self,
        preset: str | None,
        custom_channels: list[str] | None,
        stream_api_address: str,
        key_generator_address: str,
        session_name: str | None,
    ) -> None:
        source = HwinfoReader()
        atlas = AtlasWriter(
            stream_api_address,
            self._config.data_source,
            self._config.stream,
            key_generator_address,
        )

        self._start_time = time.time()
        frequency = max(1, self._config.sample_frequency_hz)
        interval_ns = int(1e9 / frequency)
        sample_period_s = 1.0 / frequency
        # One PeriodicDataPacket per second of samples.
        batch_size = frequency
        # A single worker keeps packets in the order they were produced while
        # still keeping the gRPC round-trip off the sampling loop.
        executor = ThreadPoolExecutor(max_workers=1)
        channels: list[ChannelDef] = []

        try:
            logger.info("Connecting to Stream API at %s...", stream_api_address)
            if not atlas.connect():
                self._fail("Failed to connect to Stream API. Is Docker running?")
                return
            with self._lock:
                self._status.atlas_connected = True

            logger.info("Opening HWiNFO shared memory...")
            if not source.connect():
                self._fail(
                    source.last_error
                    or "HWiNFO shared memory unavailable. Enable Settings > Main "
                    "Settings > 'Shared Memory Support' in HWiNFO."
                )
                return
            with self._lock:
                self._status.source_connected = True

            # Channels only exist once HWiNFO has been read — discover, then narrow
            # to the requested preset or explicit selection.
            try:
                readings = source.discover()
            except HwinfoUnavailable as e:
                self._fail(str(e))
                return

            all_channels = build_channels(readings, frequency)
            channels = resolve_channels(all_channels, preset, custom_channels)
            if not channels:
                self._fail(
                    f"No channels matched (preset={preset!r}). HWiNFO published "
                    f"{len(all_channels)} readings."
                )
                return

            # Derived channels are computed from the resolved set's own values
            # each tick, not read from HWiNFO — see derived_channels.py. A spec
            # whose $-references aren't in this session's channels is skipped.
            derived_specs = load_derived_specs()
            derived_pairs = resolve_derived(
                derived_specs, {ch.metric_key for ch in channels}, frequency
            )
            channels = channels + [ch for ch, _spec in derived_pairs]

            self._channels = channels
            real_channels = [ch for ch in channels if not ch.is_derived]
            source.bind_channels(real_channels)
            real_keys = [ch.metric_key for ch in real_channels]
            keys = [ch.metric_key for ch in channels]
            with self._lock:
                self._status.active_channels = keys
                self._status.channel_count = len(channels)

            session_info = source.get_session_info()
            if not session_name:
                session_name = (
                    f"{session_info['host']} HWiNFO - "
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}"
                )

            logger.info(
                "Registering %d channels with ATLAS (one round-trip each, this can "
                "take a moment)...",
                len(channels),
            )
            session_key = atlas.create_session(session_name, channels)
            if not session_key:
                self._fail("Failed to create Atlas session")
                return

            with self._lock:
                self._status.session_key = session_key

            # Critical rule 4: every batch must start exactly where the previous
            # one ended, so the trace stays continuous regardless of loop jitter.
            self._next_timestamp_ns = int(time.time() * 1e9)

            logger.info("Streaming started: %s (%d channels)", session_name, len(channels))

            while self._running:
                batch: dict[str, list[SampleValue]] = {k: [] for k in keys}
                last_telemetry: dict[str, SampleValue] = {}

                for _ in range(batch_size):
                    if not self._running:
                        break

                    loop_start = time.time()
                    telemetry = source.read_telemetry(real_keys).parameter_values

                    if derived_pairs:
                        values = {
                            k: (v.value if v.value is not None else 0.0)
                            for k, v in telemetry.items()
                        }
                        for derived_ch, spec in derived_pairs:
                            result = evaluate_derived(spec, values)
                            values[derived_ch.metric_key] = result
                            telemetry[derived_ch.metric_key] = SampleValue(
                                self._next_timestamp_ns, derived_ch.metric_key, result
                            )

                    last_telemetry = telemetry

                    for k in keys:
                        sample = telemetry.get(k)
                        if sample is None:
                            batch[k].append(SampleValue(self._next_timestamp_ns, k, 0.0))
                        elif sample.value is None:
                            batch[k].append(SampleValue(sample.timestamp, k, 0.0))
                        else:
                            batch[k].append(sample)

                    remaining = sample_period_s - (time.time() - loop_start)
                    if remaining > 0 and self._running:
                        time.sleep(remaining)

                count = len(batch[keys[0]]) if keys else 0
                if count:
                    start_ns = self._next_timestamp_ns
                    self._next_timestamp_ns += interval_ns * count
                    executor.submit(
                        self._send_data, atlas, batch, keys, last_telemetry, start_ns, interval_ns, source
                    )

        except Exception as e:
            logger.exception("Bridge error")
            with self._lock:
                self._status.error = str(e)
        finally:
            executor.shutdown(wait=True)
            atlas.end_session()
            atlas.disconnect()
            source.disconnect()

            with self._lock:
                self._status.streaming_active = False
                self._status.source_connected = False
                self._status.atlas_connected = False

            self._running = False
            logger.info("Bridge stopped")

    def _send_data(
        self,
        atlas: AtlasWriter,
        batch: dict[str, list[SampleValue]],
        keys: list[str],
        last_telemetry: dict[str, SampleValue],
        start_ns: int,
        interval_ns: int,
        source: HwinfoReader,
    ) -> None:
        count = len(batch[keys[0]]) if keys else 0
        if count:
            atlas.send_periodic_data(batch, start_ns, interval_ns)

        with self._lock:
            self._status.samples_sent += count
            for key in keys:
                sample = last_telemetry.get(key)
                if sample is not None and sample.value is not None:
                    self._status.current_values[key] = float(sample.value)
            self._status.insights = analyze(self._status.current_values, self._channels)
            self._status.elapsed_seconds = time.time() - self._start_time
            self._status.hwinfo_poll_age_seconds = source.poll_age_seconds()
