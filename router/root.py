from fastapi import APIRouter

route = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@route.get("/")
async def root():
    return {"greeting": "Welcome to student manager"}