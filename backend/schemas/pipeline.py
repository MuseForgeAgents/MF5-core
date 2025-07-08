from pydantic import BaseModel
from typing import List, Optional

class PipelineStep(BaseModel):
    step_id: str
    type: str
    model_id: Optional[str] = None
    adapter_name: Optional[str] = None
    input_keys: List[str]
    output_keys: List[str]

class PipelineConfig(BaseModel):
    pipeline_id: str
    steps: List[PipelineStep]
