# 🚀 Full Stack Daily Projects

A learning journey through full-stack web development. Each project is a small, focused application designed to understand how APIs work, frontend-backend integration, and progressive skill building.

**Goal**: Build 1 small full-stack app daily to learn concepts and best practices before moving to advanced projects.

---

## 📂 Projects

### [Project 1: FastAPI + OpenAI + React Stack](./projects/project-01-fastapi-openai/)
- **Tech**: FastAPI (Backend), React (Frontend), OpenAI API
- **Concepts**: REST APIs, LLM Integration, Frontend-Backend Communication
- **Status**: In Progress

### [Project 2: Echo App](./projects/project-02-echo-app/)
- **Tech**: FastAPI/Backend, React Frontend
- **Concepts**: Full Stack Basics, State Management, API Routing
- **Status**: In Progress

### [Project 3: AI Todo CRUD](./projects/project-03-todo-crud/)
- **Tech**: Full Stack CRUD Application
- **Concepts**: Create, Read, Update, Delete operations, Database integration
- **Status**: In Progress

---

## 🛠 Setup Instructions

### Prerequisites
- Python 3.12+
- Node.js 18+
- Git

### Initial Setup (One-time)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bsivavenu/fullstack_daily_projects.git
   cd fullstack_daily_projects
   ```

2. **Create shared Python virtual environment**:
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install each project's dependencies**:
   ```bash
   # For each project backend
   cd projects/project-01-fastapi-openai/backend
   pip install -r requirements.txt
   cd ../../../
   
   cd projects/project-02-echo-app/eco_backend
   pip install -r requirements.txt
   cd ../../../
   
   cd projects/project-03-todo-crud/backend
   pip install -r requirements.txt
   cd ../../../
   ```

4. **Install frontend dependencies**:
   ```bash
   # For each project frontend
   cd projects/project-01-fastapi-openai/frontend && npm install
   cd ../../../
   
   cd projects/project-02-echo-app/echo-frontend && npm install
   cd ../../../
   
   cd projects/project-03-todo-crud/frontend && npm install
   cd ../../../
   ```

### Running Individual Projects

Each project folder has its own setup. Navigate to the project:

```bash
cd projects/project-XX-name/
# Follow project-specific README.md
```

---

## 📋 Project Structure

```
fullstack_daily_projects/
├── .venv/                    # Shared Python virtual environment
├── .gitignore
├── README.md                 # This file
├── projects/
│   ├── project-01-fastapi-openai/
│   │   ├── backend/
│   │   ├── frontend/
│   │   └── README.md
│   ├── project-02-echo-app/
│   │   ├── eco_backend/
│   │   ├── echo-frontend/
│   │   └── README.md
│   └── project-03-todo-crud/
│       ├── backend/
│       ├── frontend/
│       └── README.md
```

---

## 🎯 Learning Path

1. **Basics**: Understanding API routes, request/response cycle
2. **Frontend Integration**: How frontend communicates with backend
3. **State Management**: Managing data across frontend-backend
4. **Databases**: Storing and retrieving data
5. **Advanced**: Authentication, deployment, optimization

---

## 💡 Tips for Learning

- **One project per day**: Focus on one concept at a time
- **Read errors carefully**: They guide you to solutions
- **Check network tabs**: Use browser DevTools to see API calls
- **Document learnings**: Add comments explaining what each endpoint does
- **Git commits**: Commit frequently with meaningful messages

---

## 🔗 Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev/)
- [REST API Best Practices](https://restfulapi.net/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

## 📝 License

Learning project - Use for educational purposes.

---

**Happy Learning! 🎓**
