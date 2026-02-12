from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, invoices
from app.db import engine
from app import models

# This line creates the tables in invoices.db automatically
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(invoices.router)