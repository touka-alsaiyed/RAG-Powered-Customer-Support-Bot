"""
LLM Utils: Connect to Ollama (Local LLM Server)
This handles all communication with Mistral via Ollama
"""

import requests
import json

# Ollama API endpoint (running on port 11435)
OLLAMA_API_URL = "http://localhost:11435/api/generate"

print("=" * 50)
print("LLM UTILS: Ollama Connection")
print("=" * 50)
print(f" Ollama endpoint: {OLLAMA_API_URL}")
print(f" Model: mistral")
print("=" * 50)

def generate_response(user_query: str, retrieved_docs: list) -> str:
    """
    Generate answer using Mistral (via Ollama) based on retrieved documents
    
    Args:
        user_query: Customer's question
        retrieved_docs: List of relevant documents from RAG system
    
    Returns:
        Generated answer from Mistral
    """
    
    # Step 1: Format context from retrieved documents
    context = "\n\n".join([
        f"[{doc['title']}]\n{doc['content']}"
        for doc in retrieved_docs
    ])
    
    # Step 2: Create system prompt
    system_prompt = """You are a helpful customer support AI.
Use ONLY the provided documents to answer customer questions accurately.
If the documents don't contain information to answer the question, say "I don't have that information."
Keep answers concise, professional, and helpful.
Answer in the same language as the question."""
    
    # Step 3: Create user message with context and question
    user_message = f"""Documents:
{context}

Customer Question: {user_query}

Answer:"""
    
    # Step 4: Create full prompt
    full_prompt = f"""{system_prompt}

{user_message}"""
    
    try:
        # Step 5: Call Ollama API
        print(f"\n📝 Query: {user_query}")
        print(f"🔍 Retrieved {len(retrieved_docs)} documents")
        print("⏳ Generating response with Mistral...")
        
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": "mistral",
                "prompt": full_prompt,
                "stream": False,
                "temperature": 0.7,  # Balance between creativity and accuracy
            },
            timeout=120  # 2 minute timeout for LLM generation
        )
        
        # Step 6: Check for errors
        if response.status_code == 200:
            result = response.json()
            answer = result.get("response", "").strip()
            
            # Clean up the answer (remove extra whitespace)
            if answer:
                print(f"✅ Generated response")
                return answer
            else:
                return "I couldn't generate an answer for this question."
        else:
            return f"Error from Ollama: {response.status_code}"
    
    except requests.exceptions.ConnectionError:
        return "❌ Error: Ollama server not running. Run: ollama serve"
    except requests.exceptions.Timeout:
        return "❌ Error: Ollama took too long to respond. Try again."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Test function
def test_llm():
    """Test LLM connection"""
    print("\n" + "=" * 50)
    print("TESTING LLM CONNECTION")
    print("=" * 50)
    
    # Create dummy documents (for testing)
    test_docs = [
        {
            "title": "Shipping",
            "content": "Standard shipping takes 5-7 business days and is FREE on orders over $50. Express shipping costs $9.99 and takes 2-3 days."
        }
    ]
    
    # Test query
    test_query = "How long does shipping take?"
    
    print(f"\nTest Query: {test_query}")
    print(f"Test Documents: {len(test_docs)}")
    
    # Generate response
    answer = generate_response(test_query, test_docs)
    
    print(f"\n📤 Answer:\n{answer}")
    print("\n" + "=" * 50)

if __name__ == "__main__":
    test_llm()