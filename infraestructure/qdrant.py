from qdrant_client import QdrantClient
from config import QDRANT_API_KEY, QDRANT_HOST, QDRANT_COLLECTION_NAME

qdrant_client = QdrantClient(
    url=QDRANT_HOST, 
    api_key=QDRANT_API_KEY,
)

def test_conection_qdrant():
    try:
        collections = qdrant_client.get_collections()
        return collections
    except Exception as e:
        return f"Error al conectar a Qdrant: {e}"

collection_name = QDRANT_COLLECTION_NAME or "collection"

def search_in_qdrant(query_vector: list[float], top_k: int = 5):
    try:
        search_result = qdrant_client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=top_k
        )

        return [
            {
                "id": point.id,
                "score": point.score,
                "payload": point.payload or {}
            }
            for point in search_result.points
        ]

    except Exception as e:
        print("Error en Qdrant:", e)
        return []