from fastapi import FastAPI
from contextlib import asynccontextmanager
from models.models import NewUser
from router.get_user import router as get_users
from db.fake_db import fake_db
import json


document = "database.json"

async def data_management():
    with open(document, "w") as file:
        json.dump(fake_db, file, indent=4)

@asynccontextmanager
async def lifepan(app: FastAPI):
    with open(document, "r") as file:
        data = json.load(file)
        fake_db[:] = data
        yield
        fake_db.clear()

app = FastAPI(lifespan=lifepan)
app.include_router(get_users)

@app.get("/")
async def root():
    return {"greeting": "Welcome to student manager"}

@app.post("/create/")
async def create_new_user(new_user: NewUser):
    fake_db.append(new_user.model_dump())
    await data_management()
    return {"user": new_user, "status": "200ok"}

@app.patch("/update")
async def update_user(index: int, new_name: str, new_last_name: str):
    user_updated = {"name": new_name, "last_name": new_last_name}
    fake_db[index] = user_updated
    await data_management()
    return {"name": new_name, "last_name": new_last_name, "message": "User updated"}

@app.delete("/delete")
async def delete_user(index: int):
    fake_db.pop(index)
    await data_management()
    return {"action": "user deleted"}