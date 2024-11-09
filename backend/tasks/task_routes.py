from fastapi import APIRouter, status, Depends, HTTPException
from ..utils.database_util import Users, Tasks, engine
from ..utils.db_queries import TQueries
from ..utils.schemas import Task
from ..auth.token_utils import get_current_user
from datetime import datetime

router = APIRouter(
    prefix="/task",
    tags=["task"]
)

task_queries = TQueries(engine, Tasks)


# All this operations must be performed when the user logs in

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task, current_user: Users = Depends(get_current_user)):
    """Create task for the user, when the task is created, this use user_id from User table to know wich task belongs to each user """
    task = Tasks(title=task.title, description=task.description, completed=task.completed,
                 task_created_at=datetime.now(), user_id=current_user["user_id"])
    return task_queries.create_task(task)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_tasks(current_user: Users = Depends(get_current_user)):
    """Gets all the user's tasks, considering their User ID"""
    tasks = task_queries.get_user_tasks(current_user["user_id"])

    return {"data": {"user": current_user["username"],
                     "result": tasks}}


@router.delete("/{task_id}")
async def delete_task(task_id: int, current_user: Users = Depends(get_current_user)):
    """Delete the task specified by the task ID"""
    return task_queries.delete_task(task_id, current_user["user_id"])


@router.put("/{task_id}")
async def update_boolean_value(task_id: int, current_user: Users = Depends(get_current_user)):
    """Changes the value of the 'completed' box from False to True, False for when it is not completed and True for when it is."""
    return task_queries.change_completed_value(task_id, current_user["user_id"])
