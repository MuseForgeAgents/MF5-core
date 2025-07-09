import os, json
from backend.storage.model_store import safe_read_json, safe_write_json

PIPELINE_ROOT = "user/pipelines"

async def run_pipeline(pipeline_id: str, input_data: dict):
    pipeline_path = os.path.join(PIPELINE_ROOT, pipeline_id)
    pipeline_file = os.path.join(pipeline_path, "pipeline.json")

    if not os.path.exists(pipeline_file):
        raise FileNotFoundError(f"Pipeline config not found for {pipeline_id}")

    with open(pipeline_file) as f:
        pipeline_config = json.load(f)

    run_record = {
        "pipeline_id": pipeline_id,
        "status": "started",
        "steps": [],
        "input": input_data
    }

    for step in pipeline_config.get("steps", []):
        step_id = step.get("step_id")
        step_type = step.get("type")
        run_record["steps"].append({
            "step_id": step_id,
            "type": step_type,
            "status": "completed"  # stub
        })

    run_record["status"] = "completed"

    safe_write_json(os.path.join(pipeline_path, "pipeline_run.json"), run_record)
    return run_record