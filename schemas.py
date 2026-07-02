from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enums import PriorityEnum

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority : PriorityEnum

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority : PriorityEnum

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    owner_username: Optional[str] = None
    priority : PriorityEnum

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str