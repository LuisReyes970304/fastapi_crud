from fastapi import APIRouter
from models.models import NewUser
from db.fake_db import fake_db
from infrastructure.data_management import data_management

route = APIRouter(
    prefix="/Create_user",
    tags=["Create_user"]
)

@route.post("/create/")
async def create_new_user(new_user: NewUser):
    fake_db.append(new_user.model_dump())
    await data_management()
    return {"user": new_user, "status": "200ok"}