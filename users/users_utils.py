from fastapi import APIRouter, status
from utils.database_util import Users, engine
from utils.db_queries import Queries

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

user_query = Queries(engine, Users)

@router.get("/me", status_code=status.HTTP_200_OK)
async def get_me():
    pass

@router.delete("/{username}")
async def delete_users(username: str):
    del_user = user_query.delete_existent_user(username)
    return del_user
