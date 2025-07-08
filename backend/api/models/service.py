from backend.storage.model_store import get_model_list, get_model_json
from backend.services.validation_service import validate_against_schema
from backend.services.replicate_api import run_prediction

async def list_models(provider=None, tags=None):
    return get_model_list(provider, tags)

async def get_model_details(model_id: str):
    return get_model_json(model_id)

async def run_prediction(model_id, input_data):
    return await run_prediction(model_id, input_data)

async def validate_model_input(model_id, input_data):
    schema = get_model_json(model_id).get("input_schema", {})
    return validate_against_schema(schema, input_data)

async def get_model_schema(model_id):
    return get_model_json(model_id).get("input_schema", {})
