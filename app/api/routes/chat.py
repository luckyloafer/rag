from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import ask_question
from app.states import document_upload_status


router = APIRouter()

SAMPLE_RESPONSE = {
    "answer": "This is a sample hardcoded response from the RAG chat API.",
    "sources": [
        {"source": "sample-document.pdf", "page": 1},
    ],
}

class ChatRequest(BaseModel):
    query: str

@router.post("/chat/{document_id}")
async def chat(document_id: str, req: ChatRequest):
    if document_id not in document_upload_status:
        return {
            "message": "Invalid document id"
        }

    if document_upload_status[document_id]["status"] != "completed":
        return {
            "message": "Document is still processing"
        }
    return ask_question(req.query)