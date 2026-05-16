from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Task
from schemas import TaskCreate, TaskUpdate, TaskResponse
from typing import List, Optional
from security import get_current_user

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    new_task = Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks(
    completed: Optional[bool] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    query = db.query(Task).filter(Task.is_deleted == False)
    
    if completed is not None:
        query = query.filter(Task.completed == completed)
    
    offset = (page - 1) * limit
    return query.offset(offset).limit(limit).all()

@router.get("/tasks/deleted", response_model=List[TaskResponse])
def get_deleted_tasks(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.is_deleted == True).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks deleted")
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    task_data = db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()
    if not task_data:
        raise HTTPException(status_code=404, detail="Task not found")
    task_data.title = task.title or task_data.title
    task_data.description = task.description or task_data.description
    task_data.completed = task.completed or task_data.completed
    db.commit()
    db.refresh(task_data)
    return task_data

@router.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.is_deleted = True
    db.commit()
    db.refresh(task)
    return task

@router.get("/stats")
def get_stats(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    total = db.query(Task).filter(Task.is_deleted == False).count()
    completed = db.query(Task).filter(Task.completed == True, Task.is_deleted == False).count()
    deleted = db.query(Task).filter(Task.is_deleted == True).count()
    pending = total - completed
    
    return {
        "total_tasks": total,
        "completed": completed,
        "pending": pending,
        "deleted": deleted
    }