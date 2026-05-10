from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Task
from schemas import TaskCreate, TaskUpdate, TaskResponse
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.is_deleted == False).all()

@router.get("/tasks/deleted",response_model=List[TaskResponse])
def get_deletedtask(db : Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.is_deleted == True).all()
    if not tasks:
        raise HTTPException(status_code=404,detail="no tasks deleted")
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}",response_model=TaskResponse)
def update_task(task_id: int ,task: TaskUpdate , db: Session = Depends(get_db)):
    task_data = db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()
    if not task_data:
        raise HTTPException(status_code=404, detail="Task not found")
    task_data.title = task.title or task_data.title
    task_data.description = task.description or task_data.description
    task_data.completed = task.completed or task_data.completed
    db.commit()
    db.refresh(task_data)
    return task_data

@router.delete("/tasks/{task_id}",response_model=TaskResponse)
def delete_task(task_id : int , db : Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=404,detail = "Task not found")
    task.is_deleted = True
    db.commit()
    db.refresh(task)
    return task


