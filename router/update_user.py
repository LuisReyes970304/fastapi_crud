from fastapi import APIRouter
from db.fake_db import fake_db
from infrastructure.data_management import data_management

router = APIRouter(
    prefix="/Upsate_User",
    tags=["Update_User"]
)

@router.patch("/update")
async def update_user(index: int, username: str, new_password: str):
    user_updated = {"username": username, "password": new_password}
    fake_db[index] = user_updated
    await data_management()
    return {"username": username, "password": new_password, "message": "User updated"}