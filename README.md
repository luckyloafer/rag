# RAG API

PDF upload + vector search (Qdrant) + chat (Google Gemini).

# 🤖 Enterprise Agentic AI Platform

A production-grade **Agentic AI** platform built using **LangGraph**, **LangChain**, **OpenAI**, **Qdrant**, **Redis**, and **FastAPI**.

This project goes beyond a traditional RAG chatbot by implementing **multi-agent orchestration**, **tool routing**, **conversation memory**, **semantic search**, **human-in-the-loop approval**, **guardrails**, **observability**, and **production-ready AI workflows**.

---

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

# 🚀 Features

- ✅ Agentic AI Workflow using LangGraph
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Multi-Agent Orchestration
- ✅ Dynamic Tool Routing
- ✅ Conversation Memory (Redis)
- ✅ Semantic Search (Qdrant)
- ✅ PDF Knowledge Base
- ✅ SQL Query Tool
- ✅ Google Search Tool
- ✅ Reflection (Critic Agent)
- ✅ Retry Mechanism
- ✅ Human-in-the-loop Approval
- ✅ Semantic Cache
- ✅ Prompt Injection Detection
- ✅ Guardrails
- ✅ LangSmith Tracing
- ✅ RAG Evaluation
- ✅ Cost Optimization
- ✅ Production Logging

---

# 🏗 Architecture

```
                          User
                            │
                            ▼

                     FastAPI API

                            │
                            ▼

                    LangGraph Workflow

                            │

         ┌──────────────────┼─────────────────┐

         ▼                  ▼                 ▼

  Memory Manager       Planner Agent     Supervisor

         │                  │

         ▼                  ▼

    Query Rewriter      Router Agent

                           │

         ┌─────────────────┼──────────────────┐

         ▼                 ▼                  ▼

      RAG Tool         SQL Tool         Google Search

         │                 │                  │

         └─────────────────┼──────────────────┘

                           ▼

                   Aggregator Agent

                           ▼

                     Critic Agent

                           │

               Context Sufficient?

               ┌────────────┴────────────┐

              YES                       NO

               │                         │

               ▼                         ▼

          Writer Agent              Retry Retrieval

               │

               ▼

      Output Guardrails

               │

               ▼

      Human Approval (Optional)

               │

               ▼

          Final Response
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | FastAPI |
| Workflow | LangGraph |
| AI Framework | LangChain |
| LLM | OpenAI GPT-4o |
| Embeddings | OpenAI Embeddings |
| Vector Database | Qdrant |
| Memory | Redis |
| Database | PostgreSQL |
| Observability | LangSmith |
| Evaluation | RAGAS |
| Monitoring | Prometheus + Grafana |
| Queue | Kafka (Future) |

---

# 📂 Project Structure

```
app/

├── agents/
│   ├── supervisor_agent.py
│   ├── planner_agent.py
│   ├── router_agent.py
│   ├── writer_agent.py
│   ├── critic_agent.py
│   ├── approval_agent.py
│   └── query_rewriter.py
│
├── api/
│   ├── chat.py
│   ├── upload.py
│   └── health.py
│
├── graph/
│   ├── workflow.py
│   └── state.py
│
├── ingestion/
│   ├── pdf_loader.py
│   ├── cleaner.py
│   ├── chunker.py
│   └── metadata.py
│
├── retrieval/
│   ├── retriever.py
│   ├── reranker.py
│   └── filters.py
│
├── tools/
│   ├── rag_tool.py
│   ├── sql_tool.py
│   ├── search_tool.py
│   └── calculator_tool.py
│
├── services/
│   ├── llm_service.py
│   ├── embedding_service.py
│   ├── vector_service.py
│   ├── memory_service.py
│   ├── cache_service.py
│   ├── guardrail_service.py
│   └── langsmith_service.py
│
├── evaluation/
│   ├── ragas_eval.py
│   └── metrics.py
│
├── prompts/
│
├── utils/
│
└── main.py
```

---

# 📄 Document Ingestion Pipeline

```
PDF Upload

↓

Text Extraction

↓

Cleaning

↓

Chunking

↓

Metadata Generation

↓

Embedding Creation

↓

Store in Qdrant
```

---

# 💬 Query Flow

```
User Question

↓

Load Conversation Memory

↓

Semantic Cache Check

↓

Planner

↓

Router

↓

Tool Selection

↓

Retrieve Documents

↓

Rerank

↓

Prompt Builder

↓

LLM

↓

Guardrails

↓

Save Memory

↓

Return Response
```

---

# 🧠 Memory Management

Conversation history is stored in Redis to support multi-turn conversations.

```
User

↓

Redis

↓

Conversation History

↓

Prompt Builder

↓

LLM

↓

Redis Update
```

Benefits

- Better follow-up understanding
- Context preservation
- Reduced clarification requests
- Lower token usage

---

# ⚡ Semantic Cache

To reduce latency and LLM costs, semantically similar queries are served directly from Redis.

```
Query

↓

Embedding

↓

Redis Vector Search

↓

Similarity > Threshold ?

       │

 YES ─────► Return Cached Answer

 NO

↓

Execute RAG

↓

Store Response
```

---

# 📚 Retrieval Pipeline

```
Query

↓

Embedding

↓

Qdrant

↓

Top K Documents

↓

Cross Encoder Reranker

↓

Top Relevant Chunks

↓

LLM
```

---

# 🧩 Chunking Strategy

- Recursive Chunking
- Fixed Size + Overlap
- Parent-Child Chunking
- Semantic Chunking
- Metadata Enrichment

Each chunk contains:

- Document Name
- Page Number
- Section
- Chunk ID
- Source

---

# 🛡 Guardrails

The platform includes multiple safety layers.

### Input Guardrails

- Prompt Injection Detection
- Jailbreak Prevention
- Query Validation

### Retrieval Guardrails

- Metadata Filtering
- Tenant Isolation
- Permission Checks

### Output Guardrails

- Hallucination Detection
- PII Detection
- Toxicity Filtering

### Tool Guardrails

- Tool Permissions
- Parameter Validation
- Human Approval

---

# 🔍 Observability

Integrated with LangSmith for:

- Agent Execution Trace
- Prompt Inspection
- Tool Calls
- Token Usage
- Latency Analysis
- Failure Debugging

---

# 📈 Evaluation

Uses RAGAS to evaluate:

- Faithfulness
- Context Precision
- Context Recall
- Answer Relevancy

---

# 💰 Cost Optimization

Implemented multiple optimization strategies.

- Conversation Memory
- Semantic Cache
- Embedding Cache
- Retrieval Cache
- Query Rewriting
- Prompt Compression
- Top-K Optimization

---

# 🔐 Production Features

- Multi-Agent Workflow
- Redis Conversation Memory
- Semantic Cache
- Retry Mechanism
- Reflection Agent
- Human Approval
- Role-Based Access Control
- Prompt Versioning
- Guardrails
- LangSmith
- RAGAS Evaluation
- Health Checks
- Structured Logging

---

# 🔮 Future Enhancements

- Kafka Event Streaming
- MCP Server Integration
- Multi-Modal RAG
- Image Retrieval
- Graph RAG
- Knowledge Graph
- Fine-Tuning Pipeline
- Agent Benchmarking
- Multi-Tenant Support
- Streaming Responses

---

# 📊 Performance Optimizations

- Redis Semantic Cache
- Connection Pooling
- Async APIs
- Batch Embeddings
- Chunk Deduplication
- Metadata Filtering
- Approximate Nearest Neighbor Search
- Cross Encoder Reranking

---

⭐ If you found this project useful, consider giving it a star!
