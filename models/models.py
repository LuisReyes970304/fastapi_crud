from pydantic import BaseModel

class NewUser(BaseModel):
    id: int
    username: str
    password: str
