from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError
from .database_util import Users
from typing import Type, Any
from fastapi import HTTPException, status


class Queries(object):

    def __init__(self, engine: Any, object: Type[Users]) -> None:
        self.engine = engine
        self.object = object

    def check_existent_user(self, username: str) -> bool:

        with Session(self.engine) as session:
            statement = select(self.object).where(
                self.object.username == username)
            result = session.exec(statement)
            return bool(result.first())
        
    def return_user(self, username: str):
        with Session(self.engine) as session:
            statement = select(self.object).where(
                self.object.username == username)
            result = session.exec(statement).one()
            return result

    def add_user(self, user: Type[Users]) -> dict:
        with Session(self.engine) as session:
            try:
                if not self.check_existent_user(user.username):
                    session.add(user)
                    session.commit()
                    return {"message": "User created successfully"}
                else:
                    return {"message": "User already exists"}
            except Exception as e:
                session.rollback()

    def delete_existent_user(self, username: str) -> dict:
        with Session(self.engine) as session:

            statement = select(self.object).where(
                self.object.username == username)
            result = session.exec(statement)
            user = result.first()

            try:
                if user:
                        session.delete(user)
                        session.commit()
                        return {"message": "User deleted"}
                else:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not in DB")
            except Exception as e:
                session.rollback()
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Can't delete user: {e}")