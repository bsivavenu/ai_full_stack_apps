# 🔧 Setup Guide for Full Stack Daily Projects

This is a monorepo with all your daily learning projects in one place.

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/bsivavenu/fullstack_daily_projects.git
cd fullstack_daily_projects
```

### 2. Activate the Shared Virtual Environment
```bash
source .venv/bin/activate
```

### 3. Install Dependencies for a Project

Choose the project you want to work on and install its backend dependencies:

**Project 1 - FastAPI + OpenAI:**
```bash
cd projects/project-01-fastapi-openai/ai-test
pip install -r requirements.txt
cd ../../..
```

**Project 2 - Echo App:**
```bash
cd projects/project-02-echo-app/eco_backend
pip install -r requirements.txt
cd ../../..
```

**Project 3 - Todo CRUD:**
```bash
cd projects/project-03-todo-crud/backend
pip install -r requirements.txt
cd ../../..
```

### 4. Install Frontend Dependencies

Navigate to the frontend folder and install Node dependencies:

```bash
cd projects/project-XX-name/frontend-folder-name
npm install
npm run dev  # or npm start
cd ../../../
```

## Structure Overview

```
fullstack_daily_projects/
├── .venv/                 ← Shared Python environment
├── README.md              ← Main documentation
├── SETUP_GUIDE.md         ← This file
├── projects/
│   ├── project-01-fastapi-openai/
│   │   ├── ai-frontend/   ← React frontend
│   │   ├── ai-test/       ← FastAPI backend
│   │   └── README.md
│   │
│   ├── project-02-echo-app/
│   │   ├── echo-frontend/ ← React frontend
│   │   ├── eco_backend/   ← Backend
│   │   └── README.md
│   │
│   └── project-03-todo-crud/
│       ├── frontend/      ← React frontend
│       ├── backend/       ← Backend
│       └── README.md
```

## Running a Project

### Start Backend
```bash
cd projects/project-XX-name/backend-folder
source ../../.venv/bin/activate  # If not already activated
python main.py  # or appropriate command
```

### Start Frontend (in another terminal)
```bash
cd projects/project-XX-name/frontend-folder
npm run dev  # or npm start
```

## Managing Dependencies

### Add a New Package to a Project
```bash
source .venv/bin/activate
cd projects/project-XX-name/backend-folder
pip install package-name
pip freeze > requirements.txt
```

### Common Commands

| Command | Purpose |
|---------|---------|
| `source .venv/bin/activate` | Activate shared Python environment |
| `deactivate` | Deactivate Python environment |
| `pip list` | See installed Python packages |
| `npm install` | Install frontend dependencies |
| `npm run dev` | Start frontend dev server |

## Tips

1. **Always activate .venv before working** - Ensures you're using the right Python version
2. **One project per terminal session** - Less confusion with dependencies
3. **Check README in each project** - Projects may have specific setup requirements
4. **Git workflow** - Commit often with meaningful messages as you learn

## Troubleshooting

**Python command not found?**
```bash
which python3
python3 --version
```

**Node command not found?**
```bash
which node
node --version
```

**Port already in use?**
- Change the port in your backend config or use a different port

**Virtual environment issues?**
```bash
# Recreate the venv
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
```

---

Happy learning! 🎓
