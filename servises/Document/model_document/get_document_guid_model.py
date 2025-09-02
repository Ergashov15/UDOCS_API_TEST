from typing import Optional
from pydantic import BaseModel

class DataModel(BaseModel):
    guid: str
    date: Optional[str] = None  # ✅ date mavjud bo'lishi ham, bo'lmasligi ham mumkin

class ResponseDocumentGuidModel(BaseModel):
    success: bool
    data: DataModel
    message: str





