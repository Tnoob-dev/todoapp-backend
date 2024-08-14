from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel, create_engine


class Tasks(SQLModel, table=True):
    task_id: Optional[int] | None = Field(default=None, primary_key=True)
    title: str
    description: str
    task_created_at: datetime
    user_id: Optional[int] | None = Field(foreign_key="users.user_id")



class Users(SQLModel, table=True, extend_existing=True):
    user_id: Optional[int] | None = Field(default=None, primary_key=True)
    username: str
    password_hashed: str
    created_at: datetime


DATABASE_URL = "postgresql://postgres:titi@localhost/apptodo"

engine = create_engine(DATABASE_URL)

def create_tables():
    SQLModel.metadata.create_all(engine)
    
create_tables()