from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from ..utils.database_util import Users, engine
from ..utils.db_queries import UQueries
from ..utils.schemas import User, UserInDB
from .token_utils import create_access_token
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from dotenv import load_dotenv
import os

ph = PasswordHasher()
user_query = UQueries(engine, Users)
router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

dotenv_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'configs', '.env')

load_dotenv(dotenv_path)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: User):
    """This route allows the user to create the account when entering the app"""
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
    """This route allows the user to enter the application and remain logged in with a time of 30 minutes until the token expires. Once logged in, they will have access to all the functions that a logged in user obtains."""
    user_dict = user_query.get_user_by_username(form_data.username)

    if not user_dict:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")

    user = UserInDB(**user_dict.dict())

    try:
        if ph.verify(user.hashed_password, form_data.password):
            token = create_access_token(username=user_dict.username, user_id=user_dict.user_id,
                                        expires_delta=timedelta(minutes=30))
            return {"access_token": token, "token_type": "bearer"}
    except VerifyMismatchError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")
    
@router.delete("/{username}")
async def delete_users(username: str):
    """This path allows the administrator to delete their account, or if also required, allows the user to delete their own account, since it is based on the ID of said user"""
    return user_query.delete_existent_user(username)
