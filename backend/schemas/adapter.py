from pydantic import BaseModel
from typing import List

class AdapterSpec(BaseModel):
    adapter_name: str
    description: str
    input_keys: List[str]
    output_keys: List[str]
    version: str
