from fastapi.testclient import TestClient
from main import app
from database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True, scope="function")
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

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
    client.post("/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_task():
    client.post("/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    login_response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "testpass123"
    })
    token = login_response.json()["access_token"]
    response = client.post("/tasks",
        json={"title": "Test Task", "description": "Testing"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["owner_username"] == "testuser"

def test_get_tasks():
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
    response = client.get("/tasks",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_user_scoping():
    # User 1 creates a task
    client.post("/auth/register", json={
        "username": "user1",
        "email": "user1@example.com",
        "password": "testpass123"
    })
    login1 = client.post("/auth/login", data={
        "username": "user1@example.com",
        "password": "testpass123"
    })
    token1 = login1.json()["access_token"]
    client.post("/tasks",
        json={"title": "User1 Task", "description": "Private"},
        headers={"Authorization": f"Bearer {token1}"}
    )

    # User 2 should NOT see user1's tasks
    client.post("/auth/register", json={
        "username": "user2",
        "email": "user2@example.com",
        "password": "testpass123"
    })
    login2 = client.post("/auth/login", data={
        "username": "user2@example.com",
        "password": "testpass123"
    })
    token2 = login2.json()["access_token"]
    response = client.get("/tasks",
        headers={"Authorization": f"Bearer {token2}"}
    )
    assert response.json() == []