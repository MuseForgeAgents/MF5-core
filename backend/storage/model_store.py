import os, json

BASE_DIR = "database/modelhub/models"

def get_model_list(provider=None, tags=None):
    models = []
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(root, file)) as f:
                    model = json.load(f)
                    if provider and provider not in model.get("id", ""):
                        continue
                    if tags and tags not in model.get("description", ""):
                        continue
                    models.append(model)
    return models

def get_model_json(model_id):
    path = os.path.join(BASE_DIR, model_id.replace("/", "_") + ".json")
    with open(path) as f:
        return json.load(f)

def safe_write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def safe_read_json(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}
