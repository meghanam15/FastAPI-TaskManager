from fastapi import FastAPI
from database import engine, Base
from routers import tasks, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "Task Manager API is running!"}