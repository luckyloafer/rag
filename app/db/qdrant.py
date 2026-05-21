import os

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore

from app.config import EMBEDDING_DIMENSION, QDRANT_COLLECTION
from app.ingestion.embedder import embeddings

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
COLLECTION_NAME = QDRANT_COLLECTION
VECTOR_SIZE = EMBEDDING_DIMENSION

client = QdrantClient(url=QDRANT_URL)

if not client.collection_exists(COLLECTION_NAME):
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
    )

vector_store = QdrantVectorStore(
    client=client,
    collection_name=COLLECTION_NAME,
    embedding=embeddings,
    validate_embeddings=False,
    validate_collection_config=False,
)
