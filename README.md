# 🚀 Task Manager REST API

A production-ready REST API built with **FastAPI** that provides secure JWT authentication, user-scoped task management, task prioritization, pagination, filtering, analytics, and automated testing.

---

## 🌐 Live Demo

🔗 https://fastapi-taskmanager.onrender.com/docs

---

# 🛠️ Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- OAuth2 Password Flow
- Passlib + Bcrypt
- Uvicorn
- Pytest

---

# ✨ Features

## Authentication

- User Registration
- Secure Login
- JWT Authentication
- OAuth2 Password Flow
- Password Hashing using Bcrypt
- Protected Endpoints

---

## Task Management

- Create Tasks
- View Tasks
- Update Tasks
- Delete Tasks (Soft Delete)
- User-Scoped Task Isolation
- Task Priority
  - Low
  - Medium
  - High
- Pagination
- Filtering
- Task Analytics

---

## Validation

- Request Validation using Pydantic
- Enum-based Priority Validation
- Invalid Priority Rejection
- Proper HTTP Status Codes

---

## Testing

Comprehensive API testing using **Pytest**

Includes tests for:

- User Registration
- User Login
- JWT Authentication
- Task Creation
- Task Retrieval
- User Isolation
- Priority Validation
- Invalid Request Handling

---

# 📂 Project Structure

```text
Task Manager API/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── enums.py
├── security.py
├── test_main.py
│
└── routers/
    ├── auth.py
    └── tasks.py
```

---

# ⚡ Installation

Clone the repository

```bash
git clone https://github.com/meghanam15/FastAPI-TaskManager.git
```

Move into the project

```bash
cd FastAPI-TaskManager
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key
```

---

# ▶️ Running the Application

```bash
uvicorn main:app --reload
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Running Tests

Run all tests

```bash
pytest -v
```

Expected output

```text
7 passed
```

---

# 📌 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT |

---

## Tasks

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a task |
| GET | `/tasks/{id}` | Get task by ID |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Soft delete task |
| GET | `/tasks/deleted` | View deleted tasks |

---

## Analytics

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/stats` | Task statistics |

---

# 📖 Example Request

Create Task

```json
{
    "title": "Study FastAPI",
    "description": "Complete backend assessment",
    "priority": "high"
}
```

Example Response

```json
{
    "id": 1,
    "title": "Study FastAPI",
    "description": "Complete backend assessment",
    "completed": false,
    "priority": "high",
    "owner_username": "meghana",
    "created_at": "2026-07-02T12:30:45"
}
```

---

# 📈 Future Improvements

- Docker Support
- PostgreSQL Integration
- Alembic Database Migrations
- Refresh Tokens
- Role-Based Access Control (RBAC)
- Task Categories
- Due Dates
- Search Endpoint
- CI/CD Pipeline using GitHub Actions

---

# 👩‍💻 Author

**Meghana M**

Python Backend Developer

- FastAPI
- Python
- REST APIs
- SQLAlchemy

GitHub

https://github.com/meghanam15

LinkedIn

https://www.linkedin.com/in/meghana-m-752747267

---

## ⭐ If you found this project useful, consider giving it a star!