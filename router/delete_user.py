from fastapi import APIRouter
from db.fake_db import fake_db
from infrastructure.data_management import data_management

router = APIRouter(
    prefix="/Delete_User",
    tags=["Delete_User"]
)

@router.delete("/delete")
async def delete_user(index: int):
    fake_db.pop(index)
    await data_management()
    return {"action": "user deleted"}