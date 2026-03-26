from fastapi import FastAPI
from api.v1.routes import router as api_v1_router
from middleware.timer import timer
from core.logging_config import setup_logging

setup_logging()
app = FastAPI(title="My API", version="1.0.0")

app.middleware("http")(timer)
app.include_router(api_v1_router, prefix="/api/v1") 