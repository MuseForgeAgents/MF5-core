from fastapi import APIRouter
from backend.services.cache_service import get_health_status

router = APIRouter()

@router.get("/")
async def index():
    return {"status": "ok", "version": "1.0.0"}

@router.get("/health")
async def health_check():
    return await get_health_status()
