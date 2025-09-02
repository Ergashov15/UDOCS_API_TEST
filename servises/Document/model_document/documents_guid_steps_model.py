from pydantic import BaseModel


class DocumentModel(BaseModel):
    guid: str


class DataModel(BaseModel):
    document: DocumentModel


class ResponseGuidStepsModel(BaseModel):
    success: bool
    data: DataModel
    message: str
