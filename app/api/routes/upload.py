import shutil
from pathlib import Path

from fastapi import APIRouter, HTTPException, UploadFile

from app.config import GOOGLE_API_KEY
from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import create_chunks
from app.services.vector_service import store_chunks

router = APIRouter()
TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True)


def _require_gemini_key():
    if not GOOGLE_API_KEY:
        raise HTTPException(
            status_code=400,
            detail=(
                "GOOGLE_API_KEY is missing in .env. "
                "Get one at https://aistudio.google.com/apikey"
            ),
        )


@router.post("/upload")
async def upload_pdf(file: UploadFile):
    _require_gemini_key()

    path = TEMP_DIR / file.filename

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = load_pdf(str(path))
    chunks = create_chunks(text)

    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="No text could be extracted from the PDF.",
        )

    store_chunks(chunks, file.filename)

    return {
        "message": "PDF uploaded successfully",
        "chunks": len(chunks),
    }
