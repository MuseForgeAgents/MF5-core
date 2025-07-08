import replicate
from backend.config import settings

replicate_client = replicate.Client(api_token=settings.REPLICATE_API_TOKEN)

async def fetch_collections(cached=False):
    return replicate_client.collections.list()

async def fetch_models(slug: str):
    return replicate_client.collections.get(slug).models

async def run_prediction(model_id: str, input_dict: dict):
    model = replicate_client.models.get(model_id)
    version = model.versions.get(model.latest_version.id)
    return version.predict(**input_dict)
