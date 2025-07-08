from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from starlette.middleware.base import BaseHTTPMiddleware

from backend.api.root import router as root_router
from backend.api.models.router import router as models_router
from backend.api.pipelines.router import router as pipelines_router
from backend.api.providers.replicate.router import router as replicate_router
from backend.api.providers.huggingface.router import router as hf_router
from backend.middleware.auth import AuthMiddleware
from backend.utils.error_handler import setup_exception_handlers

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="MuseForge Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(BaseHTTPMiddleware, dispatch=AuthMiddleware())
app.state.limiter = limiter

app.include_router(root_router, prefix="/")
app.include_router(models_router, prefix="/models")
app.include_router(pipelines_router, prefix="/pipelines")
app.include_router(replicate_router, prefix="/replicate")
app.include_router(hf_router, prefix="/huggingface")

setup_exception_handlers(app)
