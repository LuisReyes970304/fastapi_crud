from pydantic import BaseModel

class NewUser(BaseModel):
    id: int
    name: str
    last_name: str
