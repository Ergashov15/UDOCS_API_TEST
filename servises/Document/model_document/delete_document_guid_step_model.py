from pydantic import BaseModel

class DocumentDataModel(BaseModel):
    guid: str
    date: str  # yoki agar datetime bo‘lsa: datetime

class DataModel(BaseModel):
    document: DocumentDataModel

class ResponseDeleteModel(BaseModel):
    success: bool
    data: DataModel
    message: str

