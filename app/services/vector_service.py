from langchain_core.documents import Document
from app.db.qdrant import vector_store

def store_chunks(chunks, filename):

    docs = []

    for chunk in chunks:

        docs.append(
            Document(
                page_content=chunk,
                metadata={
                    "source": filename
                }
            )
        )

    vector_store.add_documents(docs)