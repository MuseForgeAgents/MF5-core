from pydantic import BaseModel
from typing import Optional, Dict

class ModelInfo(BaseModel):
    id: str
    name: str
    description: Optional[str]
    input_schema: Optional[Dict]
    output_schema: Optional[Dict]
    provider: Optional[str]
    tags: Optional[list]
