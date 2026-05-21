from app.db.qdrant import vector_store

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)

def retrieve(query: str):
    return retriever.invoke(query)