from typing import Annotated
from fastapi import FastAPI, HTTPException, status, Depends
from utils.database_util import Tasks, Users, engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from utils.db_queries import Queries
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from utils.schemas import User, UserInDB
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '.', 'configs', '.env')

load_dotenv(dotenv_path)

app = FastAPI(title="ToDoApp",
              version="1.0.0")
ph = PasswordHasher()
user_query = Queries(engine, Users)   
    

@app.get("/")
async def home():
    return {"Hello": "World!"}


@app.post("/signup")
async def signup(user: User):

    try:
        user.hashed_password = ph.hash(user.hashed_password)
        user = Users(username=user.username, hashed_password=user.hashed_password,
                     created_at=datetime.now())

        message = user_query.add_user(user)
        return message
    except Exception as e:
        print("Error: ", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="User already exists")


############
# Avance: ya sirve el login, pero solo con un usuario
# que hacer?: que sirva para todo el mundo xd
############

@app.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    
    user_dict = user_query.get_user_by_username(form_data.username)
    
    if not user_dict:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")
    
    user = UserInDB(**user_dict.dict())
    ph.verify(user.hashed_password, form_data.password)
    
    if ph.check_needs_rehash(user.hashed_password):
        user_query.update_user_hashed_password(user, ph.hash(form_data.password))
    
    return "All ok"
    
    # if not hashed_password:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail="Incorrect username or password")

    # return {"access_token": user.username, "token_type": "bearer"}
    
@app.get("/users/me")
async def get_me():
    pass

@app.delete("/users/{username}")
async def delete_users(username: str):
    del_user = user_query.delete_existent_user(username)
    return del_user
