from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int


class Data(BaseModel):
    token: Token


class ResponseAuthModel(BaseModel):
    success: bool
    data: Optional[Data]
    message: str
