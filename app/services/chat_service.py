from app.retrieval.retriever import retrieve
from app.prompts.rag_prompt import build_prompt
from app.services.llm_service import generate_answer

def ask_question(query):

    docs = retrieve(query)

    context = "\n\n".join([
        doc.page_content for doc in docs
    ])

    prompt = build_prompt(context, query)

    answer = generate_answer(prompt)

    return {
        "answer": answer,
    }