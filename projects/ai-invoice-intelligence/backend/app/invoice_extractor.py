from pypdf import PdfReader
from PIL import Image
import pytesseract
import os

def extract_text(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()

    if ext == ".pdf":
        reader = PdfReader(path)
        return "\n".join([p.extract_text() or "" for p in reader.pages])

    if ext in [".jpg", ".jpeg", ".png"]:
        image = Image.open(path)
        return pytesseract.image_to_string(image)

    raise ValueError("Unsupported file type")
