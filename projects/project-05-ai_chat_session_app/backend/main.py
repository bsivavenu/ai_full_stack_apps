# backend/main.py

from fastapi import FastAPI
from schemas import ChatRequest, ChatResponse
from chat import handle_chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    reply, history = handle_chat(req.session_id, req.message)
    return {
        "reply": reply,
        "history": history
    }
