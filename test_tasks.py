from fastapi.testclient import TestClient
from main import app
from database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import pytest

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


@pytest.fixture(autouse=True , scope="session")
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_register_user():
    response = client.post("/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 200

def test_login_user():
    response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_task():
    # Step 1: Register
    client.post("/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    
    # Step 2: Login → get token
    login_response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "testpass123"
    })
    token = login_response.json()["access_token"]
    
    # Step 3: Create task with token
    response = client.post("/tasks/", 
        json={"title": "Test Task", "description": "Testing"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_get_tasks():
    # Register + Login
    client.post("/auth/register", json={
        "username": "testuser2",
        "email": "test2@example.com",
        "password": "testpass123"
    })
    
    login_response = client.post("/auth/login", data={
        "username": "test2@example.com",
        "password": "testpass123"
    })
    token = login_response.json()["access_token"]
    
    # Get tasks
    response = client.get("/tasks/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)