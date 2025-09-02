from pydantic import BaseModel
from typing import Dict, Any


class Document(BaseModel):
    template: str
    data: Dict[str, Any]


class Data(BaseModel):
    document: Document


class ResponseTemplateModel(BaseModel):
    success: bool
    data: Data
    message: str
