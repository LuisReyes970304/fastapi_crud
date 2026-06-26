from fastapi import FastAPI
from contextlib import asynccontextmanager
from models.models import NewUser
from router.get_user import router as get_users
from router.root import route as root
from router.create_user import route as create_user

from db.fake_db import fake_db, document
from infrastructure.data_management import data_management
import json

@asynccontextmanager
async def lifepan(app: FastAPI):
    with open(document, "r") as file:
        data = json.load(file)
        fake_db[:] = data
        yield
        fake_db.clear()

app = FastAPI(lifespan=lifepan)

app.include_router(root)
app.include_router(get_users)
app.include_router(create_user)
app.include_router()

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