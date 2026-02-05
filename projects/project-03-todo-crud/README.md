# Todo CRUD App

A full-stack todo application with a FastAPI backend and React frontend.

## Tech Stack
- **Backend**: FastAPI, SQLAlchemy, SQLite
- **Frontend**: React, Vite

## Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Features
- Create, read, update, and delete todos
- Mark todos as completed
- Persistent storage with SQLite
