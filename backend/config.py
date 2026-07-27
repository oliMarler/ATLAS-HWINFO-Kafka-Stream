from dataclasses import dataclass


@dataclass
class BridgeConfig:
    stream_api_address: str = "localhost:13579"
    data_source: str = "Default"
    stream: str = "Stream1"
    # HWiNFO's own sensor polling period is 2000 ms out of the box, so sampling
    # faster than 2 Hz mostly repeats values. Lower HWiNFO's period first
    # (Settings > Sensors > Sensor polling period) if you raise this.
    sample_frequency_hz: int = 2
    default_preset: str = "essential"
    key_generator_address: str = "localhost:15379"
