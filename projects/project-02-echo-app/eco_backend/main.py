from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ---- CORS (VERY IMPORTANT for frontend) ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Request schema ----
class EchoRequest(BaseModel):
    message: str

# ---- GET endpoint ----
@app.get("/")
def health_check():
    return {"status": "Echo API running"}

# ---- POST endpoint ----
@app.post("/echo")
def echo_message(data: EchoRequest):
    return {
        "reply": f"Echo: {"hello"}"
        }
