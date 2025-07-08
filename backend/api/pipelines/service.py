import os, json
from backend.storage.model_store import safe_read_json, safe_write_json
from backend.services.pipeline_service import run_pipeline

DATA_DIR = "user/pipelines"

def list_pipelines():
    return [f for f in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, f))]

def create_pipeline(pipeline_id, config):
    path = os.path.join(DATA_DIR, pipeline_id)
    os.makedirs(path, exist_ok=True)
    safe_write_json(os.path.join(path, "pipeline.json"), config)
    return {"status": "created", "pipeline_id": pipeline_id}

def get_pipeline(pipeline_id):
    return safe_read_json(os.path.join(DATA_DIR, pipeline_id, "pipeline.json"))

def update_pipeline(pipeline_id, config):
    return create_pipeline(pipeline_id, config)

def delete_pipeline(pipeline_id):
    path = os.path.join(DATA_DIR, pipeline_id)
    if os.path.exists(path):
        for root, _, files in os.walk(path, topdown=False):
            for f in files:
                os.remove(os.path.join(root, f))
            os.rmdir(root)
        return {"status": "deleted"}
    return {"status": "not_found"}

async def execute_pipeline(pipeline_id, input_data):
    return await run_pipeline(pipeline_id, input_data)

def get_pipeline_status(pipeline_id):
    path = os.path.join(DATA_DIR, pipeline_id, "pipeline_run.json")
    return safe_read_json(path) if os.path.exists(path) else {"status": "not_started"}
