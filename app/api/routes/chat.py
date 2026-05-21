from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import ask_question

router = APIRouter()

SAMPLE_RESPONSE = {
    "answer": "This is a sample hardcoded response from the RAG chat API.",
    "sources": [
        {"source": "sample-document.pdf", "page": 1},
    ],
}

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
async def chat(req: ChatRequest):
    return ask_question(req.query)