from fastapi import FastAPI
from fastapi.responses import JSONResponse
from google.genai.errors import ClientError
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError

import app.config 

from app.api.routes.upload import router as upload_router
from app.api.routes.chat import router as chat_router

app = FastAPI()


@app.exception_handler(ChatGoogleGenerativeAIError)
async def gemini_error_handler(request, exc: ChatGoogleGenerativeAIError):
    message = str(exc)
    if "RESOURCE_EXHAUSTED" in message or "429" in message:
        return JSONResponse(
            status_code=429,
            content={
                "detail": (
                    "Gemini API quota exceeded for this model. "
                    "Try GEMINI_CHAT_MODEL=gemini-2.5-flash-lite in .env, "
                    "or wait and retry. See https://ai.google.dev/gemini-api/docs/rate-limits"
                ),
            },
        )
    return JSONResponse(status_code=502, content={"detail": message})


@app.exception_handler(ClientError)
async def google_client_error_handler(request, exc: ClientError):
    if exc.code == 429:
        return JSONResponse(
            status_code=429,
            content={"detail": "Gemini API quota exceeded. Wait a minute and retry."},
        )
    return JSONResponse(status_code=502, content={"detail": str(exc)})


@app.get("/")
def health():
    return {"status": "ok", "llm": "gemini", "embeddings": "gemini"}

app.include_router(upload_router)
app.include_router(chat_router)
