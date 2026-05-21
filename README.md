# RAG API

PDF upload + vector search (Qdrant) + chat (Google Gemini).

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your GOOGLE_API_KEY to .env
docker compose up -d
uvicorn app.main:app --reload
```

## API

- `GET /` — health check
- `POST /upload` — upload PDF (multipart field: `file`)
- `POST /chat` — `{"query": "your question"}`

Docs: http://127.0.0.1:8000/docs
