"""
RAG System FastAPI Server
Complete REST API for customer support Q&A with RAG
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_system import retrieve_relevant_docs, client as qdrant_client
from llm_utils import generate_response

print("=" * 60)
print("INITIALIZING FASTAPI SERVER")
print("=" * 60)

app = FastAPI(
    title="Customer Support RAG Bot",
    description="AI-powered customer support using Retrieval-Augmented Generation",
    version="1.0"
)

# Define request/response models
class QueryRequest(BaseModel):
    """User query request"""
    question: str
    language: str = "english"
    top_k: int = 3  # Number of documents to retrieve

class SourceDoc(BaseModel):
    """Source document metadata"""
    title: str
    similarity_score: float

class QueryResponse(BaseModel):
    """Complete response with answer and sources"""
    question: str
    answer: str
    sources: list[SourceDoc]
    documents_retrieved: int

print(" Request/Response models defined")

# ============================================================
# HEALTH CHECK ENDPOINT
# ============================================================

@app.get("/")
def health_check():
    """Health check endpoint - verify server is running"""
    return {
        "status": "healthy",
        "service": "Customer Support RAG Bot",
        "version": "1.0",
        "components": {
            "qdrant": "connected",
            "ollama": "configured"
        }
    }

# ============================================================
# MAIN RAG ENDPOINT
# ============================================================

@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    """
    Main RAG endpoint: Answer customer questions using retrieved documents
    
    Args:
        question: Customer's question
        language: Language (english, arabic, etc) - for future use
        top_k: Number of documents to retrieve (default: 3)
    
    Returns:
        QueryResponse with answer and source documents
    
    Example:
        {
            "question": "How long does shipping take?",
            "language": "english",
            "top_k": 3
        }
    """
    
    try:
        # Validate input
        if not request.question or len(request.question.strip()) == 0:
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )
        
        if len(request.question) > 500:
            raise HTTPException(
                status_code=400,
                detail="Question is too long (max 500 characters)"
            )
        
        print(f"\n📝 New Query: {request.question}")
        
        # Step 1: Retrieve relevant documents
        print(f"🔍 Retrieving top {request.top_k} documents...")
        retrieved_docs = retrieve_relevant_docs(
            query=request.question,
            top_k=request.top_k
        )
        
        if not retrieved_docs:
            raise HTTPException(
                status_code=404,
                detail="No relevant documents found for this question"
            )
        
        print(f" Retrieved {len(retrieved_docs)} documents")
        for doc in retrieved_docs:
            print(f"  - {doc['title']} (Score: {doc['similarity_score']})")
        
        # Step 2: Generate answer using LLM
        print("🤖 Generating answer with Mistral...")
        answer = generate_response(request.question, retrieved_docs)
        print(" Answer generated")
        
        # Step 3: Format sources
        sources = [
            SourceDoc(
                title=doc["title"],
                similarity_score=doc["similarity_score"]
            )
            for doc in retrieved_docs
        ]
        
        # Step 4: Return complete response
        return QueryResponse(
            question=request.question,
            answer=answer,
            sources=sources,
            documents_retrieved=len(retrieved_docs)
        )
    
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

# ============================================================
# DOCUMENTS ENDPOINT
# ============================================================

@app.get("/documents")
def list_documents():
    """Get information about all documents in the knowledge base"""
    try:
        collection_info = qdrant_client.get_collection("customer_support")
        
        return {
            "total_documents": collection_info.points_count,
            "collection_name": "customer_support",
            "status": "ready"
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving documents: {str(e)}"
        )

# ============================================================
# SEARCH ENDPOINT (Debug)
# ============================================================

@app.get("/search/{query}")
def search_documents(query: str, top_k: int = 3):
    """
    Debug endpoint: Search for documents without LLM generation
    Useful for testing semantic search independently
    """
    try:
        if not query or len(query.strip()) == 0:
            raise HTTPException(status_code=400, detail="Query cannot be empty")
        
        print(f"\n🔍 Search query: {query}")
        results = retrieve_relevant_docs(query, top_k=top_k)
        
        if not results:
            raise HTTPException(
                status_code=404,
                detail="No documents found matching the query"
            )
        
        return {
            "query": query,
            "results_count": len(results),
            "documents": [
                {
                    "title": doc["title"],
                    "content": doc["content"][:200] + "...",  # First 200 chars
                    "similarity_score": doc["similarity_score"]
                }
                for doc in results
            ]
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Search error: {str(e)}"
        )

# ============================================================
# STARTUP MESSAGE
# ============================================================

@app.on_event("startup")
async def startup_event():
    """Print startup message"""
    print("\n" + "=" * 60)
    print("🚀 CUSTOMER SUPPORT RAG BOT STARTED")
    print("=" * 60)
    print(" RAG System: Ready")
    print(" Ollama (Mistral): Ready")
    print(" Vector Database (Qdrant): Ready")
    print("\n📍 API Documentation: http://localhost:8000/docs")
    print("📊 Alternative docs: http://localhost:8000/redoc")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    import uvicorn
    
    print("=" * 60)
    print("Starting FastAPI Server...")
    print("=" * 60)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )