from typing import Annotated
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils.database_util import Tasks, Users, engine
from datetime import datetime, timedelta
from utils.db_queries import Queries
from argon2 import PasswordHasher
from utils.schemas import User, UserInDB
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.', 'configs', '.env')

load_dotenv(dotenv_path)

app = FastAPI(title="ToDoApp",
              version="1.0.0")
ph = PasswordHasher()
user_query = Queries(engine, Users)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_hash(password):
    hashed_password = ph.hash(password)
    return hashed_password


@app.get("/")
async def home():
    return {"Hello": "World!"}


@app.post("/signup")
async def signup(user: User):

    try:
        user.password = ph.hash(user.password)
        user = Users(username=user.username, password_hashed=user.password,
                     created_at=datetime.now())

        message = user_query.add_user(user)
        return message
    except Exception as e:
        print("Error: ", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="User already exists")

# Terminar el sistema de login
@app.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    
    user_dict = user_query.return_user(form_data.username).dict()
    
    if not user_dict:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = verify_hash(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.delete("/users")
async def delete_users(username: str):
    del_user = user_query.delete_existent_user(username)
    return del_user
