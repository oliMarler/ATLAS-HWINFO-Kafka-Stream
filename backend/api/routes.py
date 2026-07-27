import logging

from fastapi import APIRouter, Request

from api.models import (
    ChannelInfo,
    ChannelsResponse,
    ConfigResponse,
    ConfigUpdateRequest,
    HwinfoStatusResponse,
    PresetInfo,
    StartRequest,
    StatusResponse,
)
from bridge.channel_registry import (
    PRESET_DESCRIPTIONS,
    apply_preset,
    build_channels,
    preset_names,
)
from bridge.hwinfo_reader import READING_TYPE_NAMES, HwinfoReader, HwinfoUnavailable

logger = logging.getLogger(__name__)

router = APIRouter()


def _discover():
    """Open a short-lived view of HWiNFO's shared memory.

    Read-only mappings can coexist, so this is safe to call while the bridge is
    streaming from its own reader.
    """
    reader = HwinfoReader()
    try:
        if not reader.connect():
            raise HwinfoUnavailable(reader.last_error or "HWiNFO is not available")
        return reader.discover(), reader.header, reader.poll_age_seconds()
    finally:
        reader.disconnect()


@router.get("/status", response_model=StatusResponse)
def get_status(request: Request):
    engine = request.app.state.bridge_engine
    status = engine.get_status()
    return StatusResponse(
        source_connected=status.source_connected,
        atlas_connected=status.atlas_connected,
        streaming_active=status.streaming_active,
        session_key=status.session_key,
        samples_sent=status.samples_sent,
        elapsed_seconds=status.elapsed_seconds,
        active_channels=status.active_channels,
        error=status.error,
        current_values=status.current_values,
        insights=status.insights,
        channel_count=status.channel_count,
        hwinfo_poll_age_seconds=status.hwinfo_poll_age_seconds,
    )


@router.get("/hwinfo/status", response_model=HwinfoStatusResponse)
def get_hwinfo_status():
    try:
        _readings, header, poll_age = _discover()
    except HwinfoUnavailable as e:
        return HwinfoStatusResponse(available=False, error=str(e))
    return HwinfoStatusResponse(
        available=True,
        version=header.version,
        revision=header.revision,
        sensor_count=header.sensor_count,
        reading_count=header.reading_count,
        poll_age_seconds=poll_age,
    )


@router.get("/channels", response_model=ChannelsResponse)
def get_channels(request: Request):
    """Enumerate what HWiNFO is publishing right now, with live values.

    Discovery is deliberately done per request rather than cached — sensors come
    and go (a drive waking, a GPU leaving idle), and the picker should show the
    tree as it currently stands.
    """
    cfg = request.app.state.bridge_config
    try:
        readings, _header, _poll_age = _discover()
    except HwinfoUnavailable as e:
        return ChannelsResponse(available=False, error=str(e))

    channels = build_channels(readings, cfg.sample_frequency_hz)
    values = {r.triple: r.value for r in readings}

    return ChannelsResponse(
        available=True,
        channels=[
            ChannelInfo(
                metric_key=ch.metric_key,
                atlas_identifier=ch.atlas_identifier,
                label=ch.label,
                sensor_name=ch.sensor_name,
                units=ch.units,
                description=ch.description,
                group=ch.group,
                reading_type=READING_TYPE_NAMES.get(ch.reading_type, "Other"),
                value=values.get((ch.sensor_id, ch.sensor_instance, ch.reading_id)),
            )
            for ch in channels
        ],
        presets=[
            PresetInfo(
                name=name,
                description=PRESET_DESCRIPTIONS.get(name, ""),
                channel_count=len(apply_preset(channels, name)),
            )
            for name in preset_names()
        ],
    )


@router.post("/start")
def start_bridge(req: StartRequest, request: Request):
    engine = request.app.state.bridge_engine
    if req.custom_channels is not None and not req.custom_channels:
        return {"success": False, "error": "No channels selected"}

    success, message = engine.start(
        preset=req.preset,
        custom_channels=req.custom_channels,
        stream_api_address=req.stream_api_address,
        session_name=req.session_name,
    )
    if success:
        return {"success": True, "message": message}
    return {"success": False, "error": message}


@router.post("/stop")
def stop_bridge(request: Request):
    engine = request.app.state.bridge_engine
    success, message = engine.stop()
    return {"success": success, "message": message}


@router.get("/config", response_model=ConfigResponse)
def get_config(request: Request):
    cfg = request.app.state.bridge_config
    return ConfigResponse(
        stream_api_address=cfg.stream_api_address,
        data_source=cfg.data_source,
        stream=cfg.stream,
        sample_frequency_hz=cfg.sample_frequency_hz,
        default_preset=cfg.default_preset,
    )


@router.put("/config")
def update_config(req: ConfigUpdateRequest, request: Request):
    cfg = request.app.state.bridge_config
    if req.stream_api_address is not None:
        cfg.stream_api_address = req.stream_api_address
    if req.data_source is not None:
        cfg.data_source = req.data_source
    if req.stream is not None:
        cfg.stream = req.stream
    if req.default_preset is not None:
        cfg.default_preset = req.default_preset
    if req.sample_frequency_hz is not None:
        cfg.sample_frequency_hz = max(1, min(20, req.sample_frequency_hz))
    return {"success": True}
