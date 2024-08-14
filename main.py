from typing import Annotated
from fastapi import FastAPI, Form
from utils.database_util import Tasks, Users, engine
from sqlmodel import Session, select
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend

app = FastAPI()

@app.get("/")
async def home():
    return {"Hello": "World!"}


@app.post("/login/")
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}