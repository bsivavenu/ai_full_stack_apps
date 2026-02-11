from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
def chat(q: str):
    return {"reply": "Invoice intelligence coming soon"}
