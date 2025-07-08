import os
import json
from jsonschema import validate

def load_schema(model_id: str, provider: str) -> dict:
    schema_dir = f"database/modelhub/collections/{provider}"
    file_path = os.path.join(schema_dir, f"{model_id.replace('/', '_')}.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Schema not found: {file_path}")
    with open(file_path) as f:
        return json.load(f)

def validate_input(input_data: dict, schema: dict) -> dict:
    try:
        validate(instance=input_data, schema=schema)
        return {"valid": True}
    except Exception as e:
        return {"valid": False, "error": str(e)}
