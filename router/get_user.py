from fastapi import APIRouter
from db.fake_db import fake_db

router = APIRouter(
    prefix="/get_user",
    tags=["Get_User"]
)

@router.get("/users")
async def get_users():
    return fake_db