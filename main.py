from fastapi import FastAPI
from contextlib import asynccontextmanager

from models.models import NewUser

from router.root import route as root
from router.create_user import route as create_user
from router.get_user import router as get_users
from router.update_user import router as update_user
from router.delete_user import router as delete_user

from db.fake_db import fake_db, document
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
app.include_router(create_user)
app.include_router(get_users)
app.include_router(update_user)
app.include_router(delete_user)


