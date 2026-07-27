from pydantic import BaseModel


class ChannelInfo(BaseModel):
    metric_key: str
    atlas_identifier: str
    label: str
    sensor_name: str
    units: str
    description: str
    group: str
    reading_type: str
    value: float | None = None


class PresetInfo(BaseModel):
    name: str
    description: str
    channel_count: int


class ChannelsResponse(BaseModel):
    available: bool
    error: str | None = None
    channels: list[ChannelInfo] = []
    presets: list[PresetInfo] = []


class HwinfoStatusResponse(BaseModel):
    available: bool
    error: str | None = None
    version: int | None = None
    revision: int | None = None
    sensor_count: int | None = None
    reading_count: int | None = None
    poll_age_seconds: float | None = None


class StartRequest(BaseModel):
    preset: str | None = "essential"
    custom_channels: list[str] | None = None
    stream_api_address: str | None = None
    session_name: str | None = None


class InsightItem(BaseModel):
    level: str
    message: str


class StatusResponse(BaseModel):
    source_connected: bool = False
    atlas_connected: bool = False
    streaming_active: bool = False
    session_key: str | None = None
    samples_sent: int = 0
    elapsed_seconds: float = 0.0
    active_channels: list[str] = []
    error: str | None = None
    current_values: dict[str, float] = {}
    insights: list[InsightItem] = []
    channel_count: int = 0
    hwinfo_poll_age_seconds: float | None = None


class ConfigResponse(BaseModel):
    stream_api_address: str
    data_source: str
    stream: str
    sample_frequency_hz: int
    default_preset: str


class ConfigUpdateRequest(BaseModel):
    stream_api_address: str | None = None
    data_source: str | None = None
    stream: str | None = None
    default_preset: str | None = None
    sample_frequency_hz: int | None = None
