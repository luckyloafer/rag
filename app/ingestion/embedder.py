from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import EMBEDDING_DIMENSION, GEMINI_EMBED_MODEL, GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(
    model=GEMINI_EMBED_MODEL,
    google_api_key=GOOGLE_API_KEY,
    output_dimensionality=EMBEDDING_DIMENSION,
)
