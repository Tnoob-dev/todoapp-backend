from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str
    hashed_password: str
    
    @field_validator('username')
    def username_validation(cls, value):
        if not value:
            raise ValueError("Username can't be empty")
        return value
    
    @field_validator('hashed_password')
    def password_validation(cls, value):
        if len(value) < 4:
            raise ValueError("Password must be at least 4 characters long")
        return value

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False
    
class UserInDB(User):
    hashed_password: str
    