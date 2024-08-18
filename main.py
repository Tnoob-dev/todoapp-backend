from fastapi import FastAPI, status
from contextlib import asynccontextmanager
from utils.database_util import create_tables
from auth import auth_routes
from users import users_routes
from tasks import task_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("STARTING APP")
        create_tables()
        yield
    finally:
        print("CLOSING APP")

app = FastAPI(title="ToDoApp",
              version="1.0.0",
              lifespan=lifespan)

app.include_router(auth_routes.router)
app.include_router(task_routes.router)
app.include_router(users_routes.router)

@app.get("/", status_code=status.HTTP_200_OK)
async def home():
    return {"Hello": "World!"}