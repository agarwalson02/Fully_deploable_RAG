<h1 align="center">MultiDocChat: Fully Deployable Production RAG 🚀</h1>

<p align="center">
  <em>An advanced, production-ready Retrieval-Augmented Generation (RAG) system capable of conversational multi-document interactions.</em>
</p>

## 📖 Overview

**MultiDocChat** is a robust, scalable, and fully deployable AI application built on FastAPI and LangChain. It enables users to upload multiple documents, processes them using state-of-the-art chunking and embeddings, and provides a seamless conversational interface. 

Designed with **technical recruiters, interviewers, and founders in mind**, the architecture emphasizes maintainability, high performance, and rapid deployment readiness. It is not just a tutorial script—it is a foundation for production software.

## ✨ Key Features & Architecture Defaults

- **Advanced Retrieval Architecture (MMR):** Moves beyond naive vector similarity by utilizing Maximal Marginal Relevance (MMR) for diverse, high-quality document retrieval, avoiding repetitive AI context and answers.
- **LCEL RAG Pipelines:** Built using modern LangChain Express Language (LCEL) graphs for efficient, transparent, and lazy-evaluated conversational chains with seamlessly integrated chat history.
- **Session-Based Isolation:** Secure, atomic document ingestion mapping vector stores to unique local session IDs.
- **Lightning-Fast Builds:** Utilizes `uv` for ultra-fast dependency resolution and caching within Docker builds, significantly reducing CI/CD pipeline times.
- **Clean Architecture Principles:** Explicit separation of concerns (e.g., `ChatIngestor`, `ConversationalRAG`, `FaissManager`) offering a modular codebase that is easy to unit-test and extend.
- **Production-Grade Logging:** Standardized, structured logging via `structlog` for observability across microservice or monolith deployments.
- **Idempotent Ingestion:** Employs SHA-256 fingerprinting on document text segments to drastically reduce redundant LLM embedding API calls and duplicate context storage.

## 🛠 Tech Stack

- **Backend:** FastAPI, Python 3.12+
- **AI/LLM Framework:** Langchain (Core, Community, LCEL)
- **Model Integrations:** Groq, Google GenAI, OpenAI, Nebius (Agnostic integration layer)
- **Vector Store:** FAISS (Facebook AI Similarity Search) optimized for CPU environments.
- **Frontend:** HTML5, CSS3, Vanilla JS (FastAPI Jinja2 Templates)
- **Deployment & Infra:** Docker, Uvicorn, UV Package Manager

## 🚀 Getting Started

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd fully-deploable-rag
   ```

2. **Set up the Python Environment:**
   It's recommended to install dependencies using `uv` for unmatched speed.
   ```bash
   # Install uv globally if not present: pip install uv
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Update your `.env` file with appropriate API keys. Examples:
   ```env
   OPENAI_API_KEY=sk-...
   GROQ_API_KEY=gsk-...
   ```

4. **Run the Application locally:**
   ```bash
   python main.py
   # Or using uvicorn directly: uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Interact with the App:** Open your browser to `http://localhost:8000`

### Docker Deployment 🐳

For a true "deploy-anywhere" experience, a highly optimized `Dockerfile` is included.

```bash
docker build -t multi-doc-chat .
docker run -p 8080:8080 --env-file .env multi-doc-chat
```
_Note: The `Dockerfile` separates the dependency installation (using `uv`) and source code copy steps, maximizing Docker build layer caching._

## 🧠 Core System Workflows

1. **Ingestion (`ChatIngestor`)**: Files (PDFs, Docs, Txt) are uploaded, parsed, and split into optimized chunks (`RecursiveCharacterTextSplitter`).
2. **Embedding & Storage (`FaissManager`)**: Text strings are hashed natively. Unseen chunks are vectorized and appended to the session's FAISS index.
3. **Conversational Engine (`ConversationalRAG`)**: 
   - A **Question Contextualization Chain** factors in chat history to rewrite user queries into standalone, self-contained questions.
   - The query queries FAISS using MMR to pull up diverse and relevant document contexts.
   - The **Q&A Synthesis Chain** maps the retrieved context tightly with the user query to produce accurate, traceable responses.

## 🤝 Next Steps & Vision

Whether you are an interviewer reviewing algorithmic and architecture choices or a founder looking for a robust AI-MVP template, this project illustrates fundamental production readiness out-of-the-box.

Potential future evolutions:
* Integration of Semantic Routing for tool-use logic.
* Redis / PostgreSQL caching for distributed environments.
* Implementation of GraphRAG (Neo4j / Memgraph).

