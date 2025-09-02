from pydantic import BaseModel


class DocumentModel(BaseModel):
    guid: str
    status: str


class DataModel(BaseModel):
    document: DocumentModel


class ResponseDocumentCreateModel(BaseModel):
    success: bool
    data: DataModel
    message: str

