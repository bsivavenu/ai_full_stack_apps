# backend/app/routes/upload.py
from fastapi import APIRouter, UploadFile
from typing import List
import shutil
import os

from app.invoice_extractor import extract_text
from app.ai_processor import extract_structured_data  # <-- Import the new tool
from app.db import SessionLocal
from app.models import Invoice

router = APIRouter()

@router.post("/upload")
async def upload_invoices(files: List[UploadFile]):
    db = SessionLocal()
    results = []

    os.makedirs("data/invoices", exist_ok=True)

# backend/app/routes/upload.py

    for file in files:
        try:
            path = f"data/invoices/{file.filename}"
            with open(path, "wb") as f:
                shutil.copyfileobj(file.file, f)

            text = extract_text(path)
            ai_data = extract_structured_data(text) # <-- This is the likely crash point

            invoice = Invoice(
                filename=file.filename,
                vendor=ai_data.get("vendor"),
                total_amount=ai_data.get("total_amount"),
                # ... rest of your fields
            )
            # ... db save logic
        except Exception as e:
            print(f"CRITICAL ERROR processing {file.filename}: {e}")
            continue # Skip this file and move to the next instead of crashing

        db.add(invoice)
        db.commit()
        db.refresh(invoice)

        results.append({
            "id": invoice.id,
            "filename": invoice.filename,
            "structured_data": ai_data
        })

    db.close()

    return {
        "saved": len(results),
        "invoices": results
    }