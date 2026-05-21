from app.retrieval.retriever import retrieve
from app.prompts.rag_prompt import build_prompt
from app.services.llm_service import generate_answer
from app.services.reranker import Reranker

reranker = Reranker()

def ask_question(query):

    docs = retrieve(query)

    reranked_docs = reranker.rerank(
        query=query,
        documents=docs,
    )

    top_docs = reranked_docs[:5]

    context = "\n\n".join([
        doc.page_content for doc in top_docs
    ])

    prompt = build_prompt(context, query)

    answer = generate_answer(prompt)

    return {
        "answer": answer,
    }