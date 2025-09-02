from pydantic import BaseModel


class DataModel(BaseModel):
    url: str


class ResponseDocumentAccessModel(BaseModel):
    success: bool
    data: DataModel
    message: str
