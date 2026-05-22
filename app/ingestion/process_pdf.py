from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import create_chunks
from app.services.vector_service import store_chunks
from fastapi import HTTPException
from app.states import document_upload_status
import time


def process_pdf(document_id: str, file_path: str, filename: str):

    document_upload_status[document_id]["progress"] = 20
    text = load_pdf(file_path)
    document_upload_status[document_id]["progress"] = 50
    chunks = create_chunks(text)
    document_upload_status[document_id]["progress"] = 80
    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="No text could be extracted from the PDF.",
        )
    store_chunks(chunks, filename)
    document_upload_status[document_id] = {
        "status": "completed",
        "progress": 100,
        "chunks": len(chunks)
    }
