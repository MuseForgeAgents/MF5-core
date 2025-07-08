from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.api.models import service

router = APIRouter()

class InputData(BaseModel):
    inputs: dict

@router.get("/")
async def list_models(provider: str = None, tags: str = None):
    return await service.list_models(provider, tags)

@router.get("/{model_id}")
async def get_model_details(model_id: str):
    return await service.get_model_details(model_id)

@router.post("/{model_id}/predict")
async def predict(model_id: str, input_data: InputData):
    return await service.run_prediction(model_id, input_data.inputs)

@router.get("/{model_id}/schema")
async def get_schema(model_id: str):
    return await service.get_model_schema(model_id)

@router.post("/{model_id}/validate")
async def validate(model_id: str, input_data: InputData):
    return await service.validate_model_input(model_id, input_data.inputs)
