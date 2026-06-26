from fastapi import APIRouter
from db.fake_db import fake_db
from infrastructure.data_management import data_management

router = APIRouter(
    prefix="/Upsate_User",
    tags=["Update_User"]
)

@router.patch("/update")
async def update_user(index: int, new_name: str, new_last_name: str):
    user_updated = {"name": new_name, "last_name": new_last_name}
    fake_db[index] = user_updated
    await data_management()
    return {"name": new_name, "last_name": new_last_name, "message": "User updated"}