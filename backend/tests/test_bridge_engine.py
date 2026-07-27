"""
Engine-level tests, run against a synthetic HWiNFO section and a stub writer.

The point of interest is CLAUDE.md rule 4: consecutive batches must be exactly
contiguous, so a trace in ATLAS has no gaps. Deriving each batch's start from the
wall clock looks correct and is not — loop jitter opens a gap every batch — so it
is worth pinning down.

Run with pytest, or directly:  py backend/tests/test_bridge_engine.py
"""
import os
import sys
import threading
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bridge import bridge_engine
from bridge.hwinfo_reader import HwinfoReader
from config import BridgeConfig
from test_hwinfo_reader import READINGS, SENSORS, FakeSharedMemory, build_block

TEST_SECTION = "Local\\TestHWiNFO_engine"


class RecordingAtlasWriter:
    """Stands in for the gRPC writer, capturing what would have been sent."""

    def __init__(self, *_args, **_kwargs) -> None:
        self.batches: list[tuple[int, int, int]] = []  # (start_ns, interval_ns, count)
        self.session_channels: list = []
        self.ended = False
        self._lock = threading.Lock()

    def connect(self) -> bool:
        return True

    def create_session(self, _identifier, channels):
        self.session_channels = channels
        return "test-session-key"

    def send_periodic_data(self, data, timestamp_ns, interval_ns) -> bool:
        count = len(next(iter(data.values()))) if data else 0
        with self._lock:
            self.batches.append((timestamp_ns, interval_ns, count))
        return True

    def end_session(self) -> bool:
        self.ended = True
        return True

    def disconnect(self) -> None:
        pass


def _run_engine(preset="full", frequency=4, batches_wanted=3, timeout=20.0):
    """Run the engine against a fake section until enough batches have landed."""
    shm = FakeSharedMemory(TEST_SECTION, build_block(SENSORS, READINGS))
    writer = RecordingAtlasWriter()

    original_writer = bridge_engine.AtlasWriter
    original_reader = bridge_engine.HwinfoReader
    bridge_engine.AtlasWriter = lambda *a, **k: writer
    bridge_engine.HwinfoReader = lambda: HwinfoReader(shared_mem_name=TEST_SECTION)

    try:
        config = BridgeConfig()
        config.sample_frequency_hz = frequency
        engine = bridge_engine.BridgeEngine(config)

        started, message = engine.start(preset=preset, session_name="test")
        assert started, message

        deadline = time.time() + timeout
        while time.time() < deadline and len(writer.batches) < batches_wanted:
            time.sleep(0.1)

        status = engine.get_status()
        engine.stop()
        return writer, status
    finally:
        bridge_engine.AtlasWriter = original_writer
        bridge_engine.HwinfoReader = original_reader
        shm.close()


def test_batches_are_contiguous():
    writer, _status = _run_engine()
    assert len(writer.batches) >= 3, f"only {len(writer.batches)} batch(es) captured"

    for (start, interval, count), (next_start, _i, _c) in zip(writer.batches, writer.batches[1:]):
        expected = start + interval * count
        assert next_start == expected, (
            f"gap between batches: expected {expected}, got {next_start} "
            f"(drift {next_start - expected} ns)"
        )


def test_batch_shape_matches_sample_rate():
    frequency = 4
    writer, _status = _run_engine(frequency=frequency)
    # The last batch is short by design — stop() interrupts collection partway
    # and the engine flushes what it already has rather than dropping it.
    for start, interval, count in writer.batches[:-1]:
        assert count == frequency, f"expected {frequency} samples per batch, got {count}"
        assert interval == int(1e9 / frequency)
        assert start > 0

    _start, interval, count = writer.batches[-1]
    assert 0 < count <= frequency
    assert interval == int(1e9 / frequency)


def test_samples_sent_accumulates():
    """The counter reports a session total, not just the most recent batch."""
    writer, status = _run_engine()
    assert status.samples_sent >= sum(c for _s, _i, c in writer.batches[:-1])
    assert status.samples_sent > writer.batches[0][2]


def test_channels_are_discovered_and_registered():
    writer, status = _run_engine()
    labels = {ch.label for ch in writer.session_channels}
    assert "Total CPU Usage" in labels
    assert "GPU Temperature" in labels
    assert status.channel_count == len(writer.session_channels)
    assert writer.ended


def test_unmatched_preset_reports_an_error():
    """A preset that selects nothing must fail loudly, not stream zero channels."""
    writer, status = _run_engine(preset="drives", batches_wanted=1, timeout=5.0)
    assert writer.batches == []
    assert status.error and "No channels matched" in status.error


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
