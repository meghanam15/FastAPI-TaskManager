# 🚀 Task Manager REST API

A production-ready REST API built with FastAPI to manage study tasks, track learning progress, and practice backend engineering concepts.

## 🌐 Live Demo

https://fastapi-taskmanager.onrender.com/docs

## 🛠 Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* JWT Authentication
* OAuth2 Password Flow
* Passlib + Bcrypt
* Uvicorn
* Python 3.12

## ✨ Features

* User Registration & Login
* JWT Authentication
* OAuth2 Authorization Flow
* Password Hashing with Bcrypt
* CRUD Operations for Tasks
* User-Scoped Data Isolation
* Soft Delete Functionality
* Pagination & Filtering
* Task Analytics (`/stats`)
* Protected Routes
* Interactive Swagger Documentation

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

uvicorn main:app --reload
```

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
```

Visit:

```text
http://127.0.0.1:8000/docs
```

## 📌 API Endpoints

### Authentication

* POST `/auth/register`
* POST `/auth/login`

### Tasks

* GET `/tasks`
* POST `/tasks`
* GET `/tasks/{id}`
* PUT `/tasks/{id}`
* DELETE `/tasks/{id}`
* GET `/tasks/deleted`
* GET `/stats`

## 👩‍💻 Author

Meghana M

Python Backend Developer | FastAPI | REST APIs
