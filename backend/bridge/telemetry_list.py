from dataclasses import dataclass

from bridge.sample_value import SampleValue


@dataclass
class TelemetryList:
    parameter_values: dict[str, SampleValue]