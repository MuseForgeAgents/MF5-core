from pydantic import BaseModel
from typing import Optional, Dict

class ModelMetadata(BaseModel):
    id: str
    name: str
    description: Optional[str]
    version: Optional[str]
    verified: bool = False
    input_schema: Optional[Dict]
    output_schema: Optional[Dict]
