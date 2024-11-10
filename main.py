from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from backend.utils.database_util import create_tables
from backend.auth import auth_routes
from backend.users import users_routes
from backend.tasks import task_routes

# This function is for when the app starts running, to create the tables in the DB if its not already created.
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1", "http://localhost", "https://todoapp-frontend-delta.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(task_routes.router)
app.include_router(users_routes.router)

@app.get("/", status_code=status.HTTP_200_OK)
async def home():
    """See if the app is alive"""
    return {"Hello": "World!"}
