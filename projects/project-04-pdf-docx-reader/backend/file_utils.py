from docx import Document
from PyPDF2 import PdfReader
from io import BytesIO


def extract_text_from_docx(file_bytes: bytes) -> str:
    doc = Document(BytesIO(file_bytes))
    return "\n".join([para.text for para in doc.paragraphs])


def extract_text_from_pdf(file_bytes: bytes) -> str:
    reader = PdfReader(BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_text(filename: str, file_bytes: bytes) -> str:
    if filename.endswith(".docx"):
        return extract_text_from_docx(file_bytes)
    elif filename.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    else:
        raise ValueError("Unsupported file type")
