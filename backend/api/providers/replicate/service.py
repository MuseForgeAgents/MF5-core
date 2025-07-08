from backend.services.replicate_api import fetch_collections, fetch_models, run_prediction

async def get_collections_from_replicate():
    return await fetch_collections()

def get_cached_collections():
    return fetch_collections(cached=True)

async def sync_all_models():
    collections = await fetch_collections()
    results = {}
    for collection in collections:
        models = await fetch_models(collection["slug"])
        results[collection["slug"]] = models
    return results

async def get_models_for_collection(collection_name: str):
    return await fetch_models(collection_name)

async def run_replicate_prediction(model_id, input_data):
    return await run_prediction(model_id, input_data)
