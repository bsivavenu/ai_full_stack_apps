# AI Chatbot Backend – Session Memory (Day 4)

This backend is a **FastAPI-based session-aware chatbot service**.  
It demonstrates how to maintain **per-user conversation memory** and return contextual responses.

The focus of this project is **stateful backend design**, not AI intelligence.

---

## 🚀 Features

- Session-based conversation memory
- Remembers **last N messages per user**
- Stateless frontend → stateful backend
- Clean separation of concerns
- AI-ready architecture (OpenAI / local LLM plug-in later)

---

## 🧠 Core Idea

Each user is identified by a `session_id`.

For every incoming message:
1. The message is stored in memory
2. Previous messages for that session are retrieved
3. A response is generated using conversation history
4. The response is also stored
5. The updated conversation is returned

This is the **foundation of all real chatbots**.

---

## 📁 Folder Structure

backend/
│
├── main.py # FastAPI app + routes
├── chat.py # Chat handling logic
├── session_store.py # In-memory session management
├── schemas.py # Request / response models
└── README.md


---

## ⚙️ Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- In-memory store (Python dict + deque)

> ⚠️ No database or Redis is used intentionally to keep disk usage low.

---

## 🛠 Setup Instructions

### 1️⃣ Navigate to backend folder
```bash
cd backend

2️⃣ Initialize uv environment
uv init
uv venv

3️⃣ Install dependencies
uv add fastapi uvicorn

▶️ Run the Server
uvicorn main:app --reload


Server will start at:

http://localhost:8000


API docs available at:

http://localhost:8000/docs

🔁 API Endpoint
POST /chat

Request

{
  "session_id": "unique-session-id",
  "message": "Hello"
}


Response

{
  "reply": "You said: Hello. I remember 1 messages.",
  "history": [
    {
      "role": "user",
      "content": "Hello"
    }
  ]
}

🧩 How Session Memory Works

Each session_id maps to a message list

Messages are stored as:

{ "role": "user | assistant", "content": "text" }


Only the last 3 messages are retained

Older messages are automatically discarded

This mimics how real AI chat systems manage context windows.

# 🔌 AI Integration (Planned)

Currently, responses are dummy.

This function is the AI hook point:

def generate_ai_reply(history, user_message):
    ...


Later, this can be replaced with:

OpenAI Chat API

Local LLM (Ollama, LLaMA, Mistral)

Any custom AI logic

No other code needs to change.

⚠️ Limitations (Intentional)

In-memory storage (data resets on server restart)

Single-process memory (not shared across instances)

No authentication

These are deliberate design choices for learning and speed.

🧪 Learning Outcome

By building this backend, you learn:

Stateful API design

Session handling

Chat history management

AI-ready backend architecture

This backend is production-aligned, not a toy example.



