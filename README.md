# RAG-Powered Customer Support Bot

Production-grade Retrieval-Augmented Generation system that answers customer questions using semantic search + local LLMs.

## What It Does

1. **Retrieves** relevant documents using Qdrant + semantic search
2. **Generates** accurate answers with Mistral 7B (Ollama)
3. **Returns** answers with source attribution

## Tech Stack

- **LLM**: Mistral 7B (Ollama)
- **Vector DB**: Qdrant
- **Embeddings**: Sentence Transformers
- **API**: FastAPI
- **Language**: Python

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start Ollama server (in another terminal)
ollama pull mistral
ollama serve

# 3. Run the app
python main.py

# 4. Visit: http://localhost:8000/docs
```

## Test It

```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "How long does shipping take?"}'
```

## API Endpoints

- `POST /ask` — Answer a question using RAG
- `GET /documents` — List indexed documents
- `GET /search/{query}` — Search documents
- `GET /docs` — Interactive API documentation (Swagger UI)

## Features

✅ Semantic search with Qdrant vector DB  
✅ Local LLM (no API costs)  
✅ Source attribution  
✅ Production error handling  
✅ Input validation  
✅ Interactive documentation  

## Project Structure

```
├── main.py           # FastAPI server
├── rag_system.py     # Embeddings + vector search
├── llm_utils.py      # Ollama connection
├── docs.py    # Sample customer service docs


---

**Portfolio project demonstrating: vector databases, LLM orchestration, RAG systems, and production-grade API design.**
