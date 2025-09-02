from pydantic import BaseModel
from typing import List, Dict


class DefaultData(BaseModel):
    number: str
    date: str


class DataModel(BaseModel):
    template: str
    default: DefaultData
    document: List[dict]
    owner: List[dict]
    signers: List[dict]


class ResponseDocumentExampleModel(BaseModel):
    success: bool
    data: DataModel
    message: str
