"""
RAG System: Embeddings + Vector Database (Qdrant)
This handles document storage and semantic search
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
from docs import DOCUMENTS

print("=" * 50)
print("STEP 1: Loading Embedding Model")
print("=" * 50)

# Load embedding model (runs locally, no API needed)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
print(" Embedding model loaded")
print(f"  Model: all-MiniLM-L6-v2")
print(f"  Embedding dimension: {embedding_model.get_embedding_dimension()}")

print("\n" + "=" * 50)
print("STEP 2: Initialize Qdrant Vector Database")
print("=" * 50)

# Create Qdrant client (in-memory for testing)
client = QdrantClient(":memory:")
print(" Embedding model loaded")
print(f"  Model: all-MiniLM-L6-v2")
print(f"  Embedding dimension: {embedding_model.get_embedding_dimension()}")

print("\n" + "=" * 50)
print("STEP 2: Initialize Qdrant Vector Database")
print("=" * 50)

collection_name = "customer_support"
embedding_dim = embedding_model.get_embedding_dimension()

# Delete collection if it exists (for fresh start)
try:
    client.delete_collection(collection_name)
    print(f" Deleted existing collection (fresh start)")
except:
    pass

# Create collection
client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(
        size=embedding_dim,
        distance=Distance.COSINE
    ),
)
print(f" Collection '{collection_name}' created")
print(f"  Vector dimension: {embedding_dim}")
print(f"  Distance metric: Cosine similarity")

print("\n" + "=" * 50)
print("STEP 4: Convert Documents to Embeddings")
print("=" * 50)

points = []
for idx, doc in enumerate(DOCUMENTS):
    # Create embedding from document content
    embedding = embedding_model.encode(doc["content"]).tolist()
    
    # Create point (Qdrant's data structure)
    point = PointStruct(
        id=idx,
        vector=embedding,
        payload={
            "title": doc["title"],
            "content": doc["content"],
            "doc_id": doc["id"]
        }
    )
    points.append(point)
    print(f" Document {idx+1}: {doc['title']}")

print(f"\nTotal documents to store: {len(points)}")

print("\n" + "=" * 50)
print("STEP 5: Upload to Qdrant")
print("=" * 50)

client.upsert(
    collection_name=collection_name,
    points=points,
)
print(f" Stored {len(points)} documents in Qdrant")

# Verify
collection_info = client.get_collection(collection_name)
print(f" Collection contains {collection_info.points_count} points")

print("\n" + "=" * 50)
print("STEP 6: Test Semantic Search")
print("=" * 50)

def retrieve_relevant_docs(query: str, top_k: int = 3):
    """Search for documents relevant to a query"""
    
    # Convert query to embedding
    query_embedding = embedding_model.encode(query).tolist()
    
    # Search in Qdrant (using query_points for newer versions)
    search_results = client.query_points(
        collection_name=collection_name,
        query=query_embedding,
        limit=top_k,
        score_threshold=0.3  # Return results with similarity > 0.3
    )
    
    # Format results
    retrieved_docs = []
    for result in search_results.points:
        retrieved_docs.append({
            "title": result.payload["title"],
            "content": result.payload["content"],
            "similarity_score": round(result.score, 3)
        })
    
    return retrieved_docs

# Test with sample queries
test_queries = [
    "How long does shipping take?",
    "Can I return an item?",
    "What warranty do you offer?"
]

for query in test_queries:
    print(f"\nQuery: '{query}'")
    results = retrieve_relevant_docs(query, top_k=2)
    for i, doc in enumerate(results, 1):
        print(f"  {i}. {doc['title']} (Score: {doc['similarity_score']})")

print("\n" + "=" * 50)
print(" RAG SYSTEM READY!")
print("=" * 50)
print(f" {len(DOCUMENTS)} documents indexed")
print(f" Ready for semantic search")
print(f" Ready to connect to LLM")