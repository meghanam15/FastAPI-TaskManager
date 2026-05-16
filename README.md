# Task Manager REST API

A production-ready REST API built with FastAPI for managing tasks with full authentication and authorization.

---
## Live API
https://fastapi-taskmanager.onrender.com/docs

## Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Web framework |
| SQLite | Database |
| SQLAlchemy | ORM |
| Pydantic | Data validation |
| python-jose | JWT token creation & verification |
| Passlib + Bcrypt | Password hashing |
| OAuth2 Password Flow | Authentication standard |
| python-dotenv | Environment variable management |
| Uvicorn | ASGI server |
| Python 3.12 | Language |

---

## Features 

- User registration and login
- JWT token-based authentication
- OAuth2 password flow
- Password hashing with bcrypt (never stored as plain text)
- Full CRUD operations for tasks
- Soft delete (data preserved, not permanently removed)
- Filter tasks by completion status
- Pagination support
- `/stats` endpoint for task summary
- Protected routes (401 if no valid token)
- Environment variables for secrets
- Swagger UI for interactive API testing

---

## Project Structure

```
Task Manager API/
├── main.py           # App entry point
├── database.py       # DB connection and session
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic schemas
├── security.py       # JWT + password hashing
├── .env              # Secret keys (not pushed)
├── requirements.txt
└── routers/
    ├── tasks.py      # Task routes
    └── auth.py       # Auth routes
```

---

## Setup & Installation

```bash
git clone <https://github.com/meghanam15/FastAPI-TaskManager>
cd task-manager-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the root folder:
```
SECRET_KEY=your-secret-key-here
```

Run the development server:
```bash
uvicorn main:app --reload
```

Visit Swagger UI at: `http://127.0.0.1:8000/docs`

---

## API Endpoints

### Auth
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | /auth/register | Register a new user | No |
| POST | /auth/login | Login and receive JWT token | No |

### Tasks
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | /tasks | Get all tasks (filtering + pagination) | Yes |
| POST | /tasks | Create a new task | Yes |
| GET | /tasks/{id} | Get a specific task by ID | Yes |
| PUT | /tasks/{id} | Update a task | Yes |
| DELETE | /tasks/{id} | Soft delete a task | Yes |
| GET | /tasks/deleted | View all soft-deleted tasks | Yes |
| GET | /stats | Get task statistics | Yes |

### Query Parameters for GET /tasks
| Parameter | Type | Description |
|-----------|------|-------------|
| completed | bool | Filter by completion status |
| page | int | Page number (default: 1) |
| limit | int | Results per page (default: 10) |

---

## How Authentication Works

1. Register via `/auth/register`
2. Login via `/auth/login` — receive a JWT token
3. Pass token in every request header: `Authorization: Bearer <token>`
4. All task routes are protected — invalid or missing token returns 401

---

## Author

Meghana M — MCA Graduate | Python Backend Developer
