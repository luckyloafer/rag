import shutil
import uuid
from pathlib import Path

from fastapi import APIRouter, HTTPException, UploadFile

from app.config import GOOGLE_API_KEY
from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import create_chunks
from app.services.vector_service import store_chunks
from fastapi import BackgroundTasks
from app.ingestion.process_pdf import process_pdf
from app.states import document_upload_status



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


document_status = {}

@router.post("/upload")
async def upload_pdf(file: UploadFile, background_tasks: BackgroundTasks):
    _require_gemini_key()

    document_id = str(uuid.uuid4())

    path = TEMP_DIR / file.filename

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document_upload_status[document_id] = {
        "status": "processing",
        "progress": 0
    }

    background_tasks.add_task(process_pdf, document_id, path, file.filename)

    return {
        "document_id": document_id,
        "status": "processing",
        "filename": file.filename,
    }



@router.get("/status/{document_id}")
async def get_status(document_id: str):

    if document_id not in document_upload_status:
        return {"error": "Invalid document_id"}

    return document_upload_status[document_id]

