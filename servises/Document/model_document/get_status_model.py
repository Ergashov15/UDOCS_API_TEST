from pydantic import BaseModel
from typing import Dict

class StatusesModel(BaseModel):
    statuses: Dict[str, str]

class ResponseStatusModel(BaseModel):
    success: bool
    data: StatusesModel
    message: str

