from pydantic import BaseModel
import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    created_at: datetime.datetime