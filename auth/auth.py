from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from utils.database_util import Tasks, Users, engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from utils.db_queries import Queries
from utils.schemas import User, UserInDB
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from dotenv import load_dotenv
import os

ph = PasswordHasher()
user_query = Queries(engine, Users)
router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

dotenv_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'configs', '.env')

load_dotenv(dotenv_path)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
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

@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    
    user_dict = user_query.get_user_by_username(form_data.username)
    
    if not user_dict:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")
    
    user = UserInDB(**user_dict.dict())
    
    try:
        if ph.verify(user.hashed_password, form_data.password):
            return {"access_token": user.username, "token_type": "bearer"}
    except VerifyMismatchError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Incorrect username or password")