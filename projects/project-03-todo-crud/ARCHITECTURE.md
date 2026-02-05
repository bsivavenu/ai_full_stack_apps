# Architecture & CRUD Flow

This document explains how data flows through the application for each CRUD operation.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND (React + Vite)                 │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  App.jsx                                              │  │
│  │  - UI Components                                      │  │
│  │  - State Management (useState)                        │  │
│  │  - Event Handlers (onClick, onChange)                 │  │
│  └───────────────────────────────────────────────────────┘  │
│                           ↕ (HTTP Calls)                     │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  api.js                                               │  │
│  │  - API request functions                              │  │
│  │  - getTasks(), createTask(), updateTask(), deleteTask()│ │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           ↕ (HTTP)
              http://localhost:8000
                           ↕
┌─────────────────────────────────────────────────────────────┐
│                   BACKEND (FastAPI)                         │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  main.py                                              │  │
│  │  - @app.get("/tasks") - GET all todos                │  │
│  │  - @app.post("/tasks") - CREATE new todo             │  │
│  │  - @app.put("/tasks/{id}") - UPDATE todo             │  │
│  │  - @app.delete("/tasks/{id}") - DELETE todo          │  │
│  └───────────────────────────────────────────────────────┘  │
│                           ↕                                  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  models.py                                            │  │
│  │  - Task class definition (schema)                     │  │
│  │  - Fields: id, title, completed, created_at, etc.    │  │
│  └───────────────────────────────────────────────────────┘  │
│                           ↕                                  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  database.py                                          │  │
│  │  - SQLite connection setup                            │  │
│  │  - Database: todo.db                                  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 1. CREATE (Add a Todo)

### User Action
User types text in input field and clicks "Add" button

### Step-by-Step Flow

**Step 1: Frontend Click Event (App.jsx)**
```javascript
<button onClick={async () => {
  await createTask(title);  // Call api function
  setTitle("");             // Clear input
  loadTasks();              // Refresh list
}}>
  Add
</button>
```

**Step 2: API Call (api.js)**
```javascript
export const createTask = async (title) =>
  fetch(`http://localhost:8000/tasks?title=${title}`, { method: "POST" });
```
- Sends HTTP POST request with todo title
- URL: `http://localhost:8000/tasks?title=Buy milk`

**Step 3: Backend Receives (main.py)**
```python
@app.post("/tasks")
def create_task(title: str, db: Session = Depends(get_db)):
    task = Task(title=title)      # Create Task object
    db.add(task)                  # Add to database session
    db.commit()                   # Save to SQLite
    db.refresh(task)              # Get ID from database
    return task                   # Send back as JSON
```

**Step 4: Database Operation (todo.db)**
- Task is inserted into `tasks` table
- SQLite auto-generates ID and timestamps
- Data persists on disk

**Step 5: Response Back (app.js → App.jsx)**
- Backend returns the created task as JSON
- `loadTasks()` is called to refresh the list
- New todo appears in the UI

### Summary: Create
```
Input Field → Click Add → api.js POST → main.py → SQLite Insert → Response → UI Updates with New Todo
```

---

## 2. READ (Display All Todos)

### Trigger
- Page loads (useEffect runs)
- After any CRUD operation (Create/Update/Delete)

### Step-by-Step Flow

**Step 1: Component Mount (App.jsx)**
```javascript
useEffect(() => {
  loadTasks();  // Runs when component mounts
}, []);

const loadTasks = async () => {
  setTasks(await getTasks());  // Fetch and set state
};
```

**Step 2: API Call (api.js)**
```javascript
export const getTasks = async () =>
  fetch(`http://localhost:8000/tasks`).then(res => res.json());
```
- Sends HTTP GET request to fetch all todos

**Step 3: Backend Fetches (main.py)**
```python
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()  # Query all tasks from database
```

**Step 4: Database Query (todo.db)**
- SQLite executes: `SELECT * FROM tasks`
- Returns all task records

**Step 5: Response & Render (app.js → App.jsx)**
```javascript
{tasks.map(task => (
  <li key={task.id}>
    <input type="checkbox" checked={task.completed} />
    {task.title}
    <button>X</button>
  </li>
))}
```
- Tasks array is updated in state
- Each task renders as a list item

### Summary: Read
```
Page Load/Refresh → loadTasks() → api.js GET → main.py → SQLite Select → All Tasks → UI Renders List
```

---

## 3. UPDATE (Mark Todo as Complete)

### User Action
User clicks checkbox to toggle completed status

### Step-by-Step Flow

**Step 1: Checkbox Event (App.jsx)**
```javascript
<input
  type="checkbox"
  checked={task.completed}
  onChange={() => updateTask(task.id, !task.completed).then(loadTasks)}
/>
```

**Step 2: API Call (api.js)**
```javascript
export const updateTask = async (id, completed) =>
  fetch(`http://localhost:8000/tasks/${id}?completed=${completed}`, { 
    method: "PUT" 
  });
```
- URL example: `http://localhost:8000/tasks/1?completed=true`

**Step 3: Backend Updates (main.py)**
```python
@app.put("/tasks/{task_id}")
def update_task(task_id: int, completed: bool, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return {"error": "Task not found"}
    task.completed = completed  # Toggle status
    db.commit()                 # Save changes
    return task
```

**Step 4: Database Update (todo.db)**
- SQLite executes: `UPDATE tasks SET completed = true WHERE id = 1`
- Data persists on disk

**Step 5: Response & Refresh**
- Backend returns updated task
- `loadTasks()` refreshes the list
- Checkbox state updates in UI

### Summary: Update
```
Checkbox Click → updateTask() → api.js PUT → main.py → SQLite Update → Response → UI Reflects Change
```

---

## 4. DELETE (Remove Todo)

### User Action
User clicks "X" button next to a todo

### Step-by-Step Flow

**Step 1: Delete Button Click (App.jsx)**
```javascript
<button onClick={() => deleteTask(task.id).then(loadTasks)}>X</button>
```

**Step 2: API Call (api.js)**
```javascript
export const deleteTask = async (id) =>
  fetch(`http://localhost:8000/tasks/${id}`, { method: "DELETE" });
```
- URL example: `http://localhost:8000/tasks/1`

**Step 3: Backend Deletes (main.py)**
```python
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return {"error": "Task not found"}
    db.delete(task)              # Mark for deletion
    db.commit()                  # Permanently delete
    return {"message": "Task deleted"}
```

**Step 4: Database Delete (todo.db)**
- SQLite executes: `DELETE FROM tasks WHERE id = 1`
- Record is permanently removed

**Step 5: Response & Refresh**
- Backend returns success message
- `loadTasks()` refreshes the list
- Todo disappears from UI

### Summary: Delete
```
Click X → deleteTask() → api.js DELETE → main.py → SQLite Delete → Response → UI List Updates
```

---

## File Responsibilities

| File | Role | Responsibility |
|------|------|-----------------|
| **App.jsx** | Frontend Logic | UI rendering, state management, event handling |
| **api.js** | Communication | HTTP requests to backend endpoints |
| **main.py** | Backend Logic | API endpoints, request processing, business logic |
| **models.py** | Data Schema | Task structure and database fields |
| **database.py** | Database Setup | SQLite connection and session management |
| **todo.db** | Persistence | Actual data storage |

---

## Data Flow Summary

```
┌─────────────────────────────────────────────────────────────┐
│ All CRUD Operations Follow This Pattern:                    │
├─────────────────────────────────────────────────────────────┤
│ 1. User interacts with UI (click, type, change)            │
│ 2. Event handler in App.jsx triggers                        │
│ 3. Function calls api.js with required data                 │
│ 4. api.js sends HTTP request (GET/POST/PUT/DELETE)         │
│ 5. main.py receives request and processes it               │
│ 6. Database operation occurs (select/insert/update/delete)  │
│ 7. Backend sends response with result                       │
│ 8. Frontend receives response via api.js                    │
│ 9. App.jsx updates state                                    │
│ 10. UI re-renders with new data                            │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Points

- **Frontend & Backend are separate**: They communicate only via HTTP
- **Database is persistent**: All changes are saved to `todo.db`
- **Stateless Backend**: Each request is independent
- **React State is temporary**: Data refreshes from backend after each operation
- **CORS Enabled**: Frontend on different port can access backend API
