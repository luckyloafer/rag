def build_prompt(context, query, history):

    return f"""
You are an enterprise AI assistant.

Use ONLY the provided context.

If answer is not found,
say "I could not find relevant information."

Conversation History:
{history}

Context:
{context}

Question:
{query}
"""