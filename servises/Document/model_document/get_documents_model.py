from pydantic import BaseModel
from typing import List, Optional


class DocumentItem(BaseModel):
    id: int
    service_id: int
    guid: str
    # kerakli boshqa fieldlar ham shu yerda

class DocumentsData(BaseModel):
    current_page: int
    data: List[DocumentItem]
    from_: Optional[int] = None
    last_page: Optional[int] = None
    per_page: Optional[int] = None
    to: Optional[int] = None
    total: Optional[int] = None

    class Config:
        fields = {'from_': 'from'}  # because `from` is a reserved word in Python


class ResponseGetDocumentsModel(BaseModel):
    success: bool
    data: dict  # <- real structure is data={"documents": {...}}, so we will parse this in post_init or refactor further
    message: str





