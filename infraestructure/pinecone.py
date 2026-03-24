from pinecone import Pinecone
from config import PINECONE_API_KEY, PINECONE_INDEX_NAME
from typing import cast, Any

pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(PINECONE_INDEX_NAME) 

def test_connection_pinecone():
    try:
        indexes = pc.list_indexes()
        return {
            "success": True,
            "indexes": list(indexes)
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
    
def search_in_pinecone(query_vector: list[float], top_k: int = 5):
    try:
        result = index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True
        )

        matches = getattr(result, "matches", [])

        return [
            {
                "id": m.id,
                "score": m.score,
                "payload": m.metadata or {}
            }
            for m in matches
        ]

    except Exception as e:
        print("Error en Pinecone:", e)
        return []