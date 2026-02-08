from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from file_utils import extract_text
from ai import summarize_text

app = FastAPI()

# CORS (for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production: restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_bytes = await file.read()

    extracted_text = extract_text(file.filename, file_bytes)

    if not extracted_text.strip():
        return {"error": "No readable text found in document"}

    summary = summarize_text(extracted_text)

    return {
        "filename": file.filename,
        "summary": summary
    }
