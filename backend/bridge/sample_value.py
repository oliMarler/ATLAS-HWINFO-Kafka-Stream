from dataclasses import dataclass
from typing import Optional


@dataclass
class SampleValue:
    timestamp: int
    parameter: str
    value: Optional[float] = None