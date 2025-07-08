from fastapi import APIRouter
from backend.api.providers.replicate import service

router = APIRouter(prefix="/replicate")

@router.post("/collections/sync")
async def sync_collections():
    return await service.get_collections_from_replicate()

@router.post("/models/sync")
async def sync_models():
    return await service.sync_all_models()

@router.get("/collections")
async def list_cached_collections():
    return service.get_cached_collections()

@router.get("/models/{collection_name}")
async def get_models_by_collection(collection_name: str):
    return service.get_models_for_collection(collection_name)

@router.post("/models/{model_id}/predict")
async def predict(model_id: str, input_data: dict):
    return await service.run_replicate_prediction(model_id, input_data)
