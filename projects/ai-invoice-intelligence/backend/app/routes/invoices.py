from fastapi import APIRouter
from app.db import SessionLocal
from app.models import Invoice

router = APIRouter()

@router.get("/invoices")
def list_invoices():
    db = SessionLocal()
    invoices = db.query(Invoice).all()
    db.close()

    return [
        {
            "id": i.id,
            "filename": i.filename,
            "file_type": i.file_type,
            "created_at": i.created_at
        }
        for i in invoices
    ]
