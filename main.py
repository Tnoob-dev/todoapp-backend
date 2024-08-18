from fastapi import FastAPI, status
from auth import auth
from users import users_utils


app = FastAPI(title="ToDoApp",
              version="1.0.0")
app.include_router(auth.router)
app.include_router(users_utils.router) 

@app.get("/", status_code=status.HTTP_200_OK)
async def home():
    return {"Hello": "World!"}