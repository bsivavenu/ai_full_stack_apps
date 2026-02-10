from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend container + browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For learning only (not production safe)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = [
    {"id": 1, "title": "Learn Docker"},
    {"id": 2, "title": "Understand Containers"},
    {"id": 3, "title": "Connect Frontend to Backend"},
]

@app.get("/todos")
def get_todos():
    return todos
