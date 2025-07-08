from pydantic import BaseModel
from typing import List, Dict

class CollectionSchema(BaseModel):
    name: str
    slug: str
    description: str
    models: List[Dict]
