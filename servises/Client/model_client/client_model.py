from pydantic import BaseModel

class DataModel(BaseModel):
    url: str
    auth_type: int
    username: str
    password: str
    token: str

class ResponseConfigUpdateModel(BaseModel):
    success: bool
    data: DataModel
    message: str
