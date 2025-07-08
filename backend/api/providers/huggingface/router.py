from fastapi import APIRouter
from backend.api.providers.huggingface import service

router = APIRouter(prefix="/huggingface")

@router.post("/models/sync")
async def sync_hf_models():
    return await service.get_models_from_huggingface()

@router.get("/models")
async def list_cached_models():
    return service.list_cached_models()

@router.post("/models/{model_id}/predict")
async def hf_predict(model_id: str, input_data: dict):
    return await service.run_hf_prediction(model_id, input_data)

@router.get("/models/{model_id}/info")
async def model_info(model_id: str):
    return await service.get_model_info(model_id)
