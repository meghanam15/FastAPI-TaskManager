# 🚀 Task Manager REST API

A production-ready REST API built with FastAPI featuring JWT authentication, 
user-scoped task management, pagination, filtering, analytics, and automated testing.

## 🌐 Live Demo
https://fastapi-taskmanager.onrender.com/docs

## 🛠 Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- OAuth2 Password Flow
- Passlib + Bcrypt
- Uvicorn
- Python 3.12

## ✨ Features
- User Registration & Login
- JWT Authentication
- OAuth2 Authorization Flow
- Password Hashing with Bcrypt
- CRUD Operations for Tasks
- User-Scoped Data Isolation
- Soft Delete Functionality
- Pagination & Filtering
- Task Analytics (`/stats`)
- Protected Routes
- Interactive Swagger Documentation

## 📂 Project Structure
```text
Task Manager API/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── security.py
└── routers/
    ├── auth.py
    └── tasks.py
```

## ⚡ Quick Start

```bash
git clone https://github.com/meghanam15/FastAPI-TaskManager.git
cd FastAPI-TaskManager
pip install -r requirements.txt
```

Create a `.env` file:
```env
SECRET_KEY=your-secret-key
```

Run the server:
```bash
uvicorn main:app --reload
```

Visit: http://127.0.0.1:8000/docs

## 🧪 Testing

```bash
pytest test_main.py -v
```

Test coverage includes authentication flows, CRUD operations, and user-scoped data isolation.

## 📌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT token |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | Get all tasks (paginated, filterable) |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/{id}` | Get a specific task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Soft delete a task |
| GET | `/tasks/deleted` | View soft-deleted tasks |
| GET | `/stats` | Get task analytics |

## 👩‍💻 Author
Meghana M — Python Backend Developer | FastAPI | REST APIs  
[LinkedIn](https://in.linkedin.com/in/meghana-m-752747267) | [GitHub](https://github.com/meghanam15)
