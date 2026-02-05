from pydantic import BaseModel
from typing import Optional

# ----------- INPUT FOR EXTRACT API -----------

class TextInput(BaseModel):
    text: str


# ----------- TASK SCHEMAS -----------

class TaskCreate(BaseModel):
    description: str
    owner: Optional[str] = None
    deadline: Optional[str] = None
    priority: str


class TaskOut(TaskCreate):
    id: int
    completed: bool

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
