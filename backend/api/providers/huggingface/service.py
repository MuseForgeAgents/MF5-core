from huggingface_hub import HfApi

hf_api = HfApi()

async def get_models_from_huggingface(limit=100):
    models = hf_api.list_models(limit=limit)
    return [m.modelId for m in models]

def list_cached_models():
    return ["stub-hf-model"]

async def get_model_info(model_id: str):
    return hf_api.model_info(model_id).dict()

async def run_hf_prediction(model_id: str, input_data: dict):
    return {"model_id": model_id, "output": "mocked result"}
