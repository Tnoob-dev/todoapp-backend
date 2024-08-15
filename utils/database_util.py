from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel, create_engine
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'configs', '.env')

load_dotenv(dotenv_path)

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

engine = create_engine(os.getenv("DATABASE_URL"))

def create_tables():
    SQLModel.metadata.create_all(engine)
    
create_tables()