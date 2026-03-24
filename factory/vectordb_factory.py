from abc import ABC, abstractmethod
from infraestructure.pinecone import search_in_pinecone, test_connection_pinecone
from infraestructure.qdrant import search_in_qdrant, test_conection_qdrant
class VectorDBService(ABC):
    @abstractmethod
    def test_bd(self):
        pass
    @abstractmethod
    def search(self, query_vector: list[float], top_k: int = 4):
        pass

class PineconeService(VectorDBService):
    def test_bd(self):
        variable = test_connection_pinecone()
        
        return variable["success"]
        #return test_connection_pinecone()
    
    def search(self, query_vector: list[float], top_k: int = 4 ):
        return search_in_pinecone(query_vector, top_k)
class QdrantService(VectorDBService):
    def test_bd(self):
        return test_conection_qdrant()
    
    def search(self, query_vector: list[float], top_k: int = 4):
        # Implementa la lógica para realizar una búsqueda en Qdrant
        return search_in_qdrant(query_vector, top_k)

class VectorDBFactory:
    @staticmethod
    def get_vectordb_service(vectordb_name: str) -> VectorDBService:
        if vectordb_name == "pinecone":
            return PineconeService()
        elif vectordb_name == "qdrant":
            return QdrantService()
        else:
            raise ValueError(f"VectorDB '{vectordb_name}' no soportada")