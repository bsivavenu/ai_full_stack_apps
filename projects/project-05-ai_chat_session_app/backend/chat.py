# backend/chat.py

from session_store import add_message, get_history

def generate_ai_reply(history, user_message):
    # TEMP AI logic (replace with OpenAI later)
    return f"You said: {user_message}. I remember {len(history)} messages."

def handle_chat(session_id: str, message: str):
    add_message(session_id, "user", message)

    history = get_history(session_id)
    reply = generate_ai_reply(history, message)

    add_message(session_id, "assistant", reply)

    return reply, get_history(session_id)
