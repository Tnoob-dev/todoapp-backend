from typing import Annotated
from jose import jwt, JWTError
from datetime import datetime, timedelta, UTC
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'configs', '.env')

load_dotenv(dotenv_path)

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {
        'username': username,
        'id': user_id
    }
    
    expires = datetime.now(UTC) + expires_delta
    encode.update({'exp': expires})

    return jwt.encode(encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))

oauth2scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(jwebtoken: Annotated[str, Depends(oauth2scheme)]):
    try:
        payload = jwt.decode(jwebtoken, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        username: str = payload.get('username')
        user_id: int = payload.get('id')

        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Couldn't validate user",
                                headers={"WWW-Authenticate": "Bearer"})
        return {"username": username, "user_id": user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Couldn't validate user",
                                headers={"WWW-Authenticate": "Bearer"})