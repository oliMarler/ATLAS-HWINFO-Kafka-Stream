import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routes import router
from bridge.bridge_engine import BridgeEngine
from config import BridgeConfig

app = FastAPI(title="HWiNFO ATLAS Bridge")

bridge_config = BridgeConfig()
bridge_engine = BridgeEngine(bridge_config)

app.state.bridge_engine = bridge_engine
app.state.bridge_config = bridge_config

app.include_router(router, prefix="/api")

frontend_dir = Path(__file__).parent.parent / "frontend"
app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")


@app.on_event("shutdown")
def shutdown():
    if bridge_engine.is_running():
        bridge_engine.stop()
