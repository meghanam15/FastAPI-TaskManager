from sqlalchemy import Column, Integer, String, Boolean, DateTime , Enum
from sqlalchemy.sql import func
from database import Base
from enums import PriorityEnum

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    owner_username = Column(String, nullable=False) 
    priority = Column(Enum(PriorityEnum), default=PriorityEnum.Medium, nullable=False) 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)