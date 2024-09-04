from typing import Annotated
from fastapi import APIRouter, status, Depends, HTTPException
from ..utils.database_util import Users, engine
from ..utils.db_queries import UQueries
from ..auth.token_utils import get_current_user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

user_query = UQueries(engine, Users)

@router.get("/me", status_code=status.HTTP_200_OK)
async def get_me(user: Annotated[dict, Depends(get_current_user)]):
    """Get user information once logged into the app"""
    try:
        return {"user_details": user}
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
