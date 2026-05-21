from app.retrieval.retriever import retrieve
from app.prompts.rag_prompt import build_prompt
from app.services.llm_service import generate_answer
from app.services.reranker import Reranker
from app.services.memory_service import memory

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

    history = memory.load_memory_variables({})

    prompt = build_prompt(
        context=context, 
        query=query,
        history=history["chat_history"],
    )

    answer = generate_answer(prompt)

    memory.save_context(
        {"input": query},
        {"output": answer}
    )

    return {
        "answer": answer,
    }