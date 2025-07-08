from fastapi import APIRouter
from backend.api.pipelines import service
from pydantic import BaseModel

router = APIRouter()

class PipelineConfig(BaseModel):
    pipeline_id: str
    config: dict

@router.get("/")
async def list_pipelines():
    return service.list_pipelines()

@router.post("/")
async def create_pipeline(pipeline: PipelineConfig):
    return service.create_pipeline(pipeline.pipeline_id, pipeline.config)

@router.get("/{pipeline_id}")
async def get_pipeline(pipeline_id: str):
    return service.get_pipeline(pipeline_id)

@router.put("/{pipeline_id}")
async def update_pipeline(pipeline_id: str, config: dict):
    return service.update_pipeline(pipeline_id, config)

@router.delete("/{pipeline_id}")
async def delete_pipeline(pipeline_id: str):
    return service.delete_pipeline(pipeline_id)

@router.post("/{pipeline_id}/execute")
async def execute_pipeline(pipeline_id: str, input_data: dict):
    return await service.execute_pipeline(pipeline_id, input_data)

@router.get("/{pipeline_id}/status")
async def get_status(pipeline_id: str):
    return service.get_pipeline_status(pipeline_id)
