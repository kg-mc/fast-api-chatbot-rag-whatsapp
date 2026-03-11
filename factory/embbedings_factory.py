from abc import ABC, abstractmethod
from urllib import response
from urllib import response
from config import EMBEDDINGS_MODEL_NAME_HF, EMBEDDINGS_MODEL_NAME_GEMINI
from sentence_transformers import SentenceTransformer
from google.genai import Client
import torch


class EmbeddingsService(ABC):
    model: SentenceTransformer
    instruction: str
    @abstractmethod
    def generate(self):
        pass
    
    @abstractmethod
    def embed_query(self, query: str) -> list[float]:
        pass

class HuggingFaceEmbeddingsService(EmbeddingsService):
    def __init__(self, model_name: str):
        self.model_name = model_name
        # Aquí podrías cargar el modelo de Hugging Face si es necesario
    def generate(self):
        if self.model_name == "BAAI/bge-m3":
            self.model = SentenceTransformer("BAAI/bge-m3")
            self.instruction = "Represent this question for retrieving supporting documents: "
        if self.model is None:
            raise ValueError("Modelo de embeddings no inicializado")
    def embed_query(self, query: str) -> list[float]:
        embedding = self.model.encode(
            [self.instruction + query],
            normalize_embeddings=True
        )
        return embedding[0].tolist()
    
class GeminiEmbeddingsService(EmbeddingsService):
    def __init__(self, model_name: str):
        self.model_name = model_name
        # Aquí podrías cargar el modelo de Gemini si es necesario
    def generate(self):
        self.client = Client()
    def embed_query(self, query: str) -> list[float]:
        response = self.client.models.embed_content(
            model=self.model_name,
            contents=query
        )
        
        if not response.embeddings:
            raise ValueError("No se generó embedding para la query")
        
        embedding_vector = torch.tensor(response.embeddings[0].values)
        
        return embedding_vector.tolist()
    

class EmbeddingsFactory:
    @staticmethod
    def create_embeddings_service(embeddings_type: str, model_name: str = "") -> EmbeddingsService:
        if embeddings_type == "huggingface":
            if model_name == "":
                model_name = str(EMBEDDINGS_MODEL_NAME_HF)
            return HuggingFaceEmbeddingsService(model_name)
        elif embeddings_type == "gemini":
            if model_name == "":
                model_name = str(EMBEDDINGS_MODEL_NAME_GEMINI)
            return GeminiEmbeddingsService(model_name)
        else:
            raise ValueError(f"Tipo de embeddings no soportado: {embeddings_type}")