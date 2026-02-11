from fastapi import APIRouter, UploadFile
from typing import List
import shutil
import os

from app.invoice_extractor import extract_text
from app.db import SessionLocal
from app.models import Invoice

router = APIRouter()

@router.post("/upload")
async def upload_invoices(files: List[UploadFile]):
    db = SessionLocal()
    results = []

    os.makedirs("data/invoices", exist_ok=True)

    for file in files:
        path = f"data/invoices/{file.filename}"

        with open(path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        text = extract_text(path)

        invoice = Invoice(
            filename=file.filename,
            file_type=file.content_type,
            raw_text=text
        )

        db.add(invoice)
        db.commit()
        db.refresh(invoice)

        results.append({
            "id": invoice.id,
            "filename": invoice.filename
        })

    db.close()

    return {
        "saved": len(results),
        "invoices": results
    }
