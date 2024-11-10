from sqlmodel import Session, select
from .database_util import Users, Tasks
from typing import Type, Any
from fastapi import HTTPException, status


class UQueries(object):

    def __init__(self, engine: Any, object: Type[Users]) -> None:
        self.engine = engine
        self.object = object

    def get_user_by_username(self, username: str) -> (Users | None):
        with Session(self.engine) as session:
            statement = select(self.object).where(
                self.object.username == username)
            result = session.exec(statement).first()
            return result

    def check_existent_user(self, username: str) -> bool:
        return bool(self.get_user_by_username(username))

    def add_user(self, user: Type[Users]) -> dict:
        with Session(self.engine) as session:
            try:
                if not self.check_existent_user(user.username):
                    session.add(user)
                    session.commit()
                    return {"message": "User created successfully"}
                else:
                    return {"message": "User already exists"}
            except:
                session.rollback()

    def delete_existent_user(self, username: str) -> dict:
        with Session(self.engine) as session:
            try:
                statement = select(self.object).where(
                    self.object.username == username)
                result = session.exec(statement)
                user = result.first()

                if user:
                        session.delete(user)
                        session.commit()
                        return {"message": "User deleted"}
                else:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                session.rollback()
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't delete user. ERROR: {e}")
                
class TQueries(object):
    def __init__(self, engine: Any, object: Type[Tasks]) -> None:
        self.engine = engine
        self.object = object
        
    def create_task(self, task: Type[Tasks]) -> dict:
        with Session(self.engine) as session:
            try:
                session.add(task)
                session.commit()
                return {"message": "Task added"}
            except Exception as e:
                session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    def get_user_tasks(self, user_id: int) -> list[Tasks]:
        with Session(self.engine) as session:
            try:
                statement = select(self.object).where(self.object.user_id == user_id)
                result = session.exec(statement)
                return [i for i in result]
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    def change_completed_value(self, task_id: int, user_id: int) -> (Tasks | None):
        with Session(self.engine) as session:
            try:
                statement = select(self.object).where(self.object.user_id == user_id).where(self.object.task_id == task_id)
                result = session.exec(statement)
                task = result.first()
                
                if not task.completed:
                    task.completed = True
                else:
                    task.completed = False
                    
                session.add(task)
                session.commit()
                session.refresh(task)
                return task
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def delete_task(self, task_id: int, user_id: int) -> dict[str, str]:
        with Session(self.engine) as session:
            try:
                statement = select(self.object).where(self.object.user_id == user_id).where(Tasks.task_id == task_id)
                result = session.exec(statement)
                task = result.first()
                
                if task:
                    session.delete(task)
                    session.commit()
                    return {"message": "Task deleted"}
                else:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                session.rollback()
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail=f"Can't delete task. ERROR: {e}")
            