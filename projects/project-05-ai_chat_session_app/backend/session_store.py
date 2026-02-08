# backend/session_store.py

from collections import defaultdict, deque

MAX_HISTORY = 3

# session_id -> deque of messages
sessions = defaultdict(lambda: deque(maxlen=MAX_HISTORY))

def add_message(session_id: str, role: str, content: str):
    sessions[session_id].append({
        "role": role,
        "content": content
    })

def get_history(session_id: str):
    return list(sessions[session_id])
