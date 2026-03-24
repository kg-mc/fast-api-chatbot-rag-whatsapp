from abc import ABC, abstractmethod
from openai import OpenAI
from config import EMBEDDINGS_MODEL_NAME_GEMINI
from google.genai import Client


class EmbeddingsService(ABC):
    @abstractmethod
    def generate(self):
        pass
    
    @abstractmethod
    def embed_query(self, query: str) -> list[float]:
        pass

    
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
        embeddings = response.embeddings
        if not embeddings:
            raise ValueError("No se generó embedding para la query")
        values = embeddings[0].values
        if values is None:
            raise ValueError("Embedding inválido")
        return values

class OpenAIEmbeddingsService(EmbeddingsService):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = OpenAI()
    def generate(self):
        pass
    def embed_query(self, query: str) -> list[float]:
        response = self.client.embeddings.create(
            model=self.model_name,
            input=query
        )

        if not response.data:
            raise ValueError("No se generó embedding para la query")

        embedding_vector = response.data[0].embedding

        return embedding_vector

class EmbeddingsFactory:
    @staticmethod
    def create_embeddings_service(embeddings_type: str, model_name: str = "") -> EmbeddingsService:
        if embeddings_type == "gemini":
            if model_name == "":
                model_name = str(EMBEDDINGS_MODEL_NAME_GEMINI)
            return GeminiEmbeddingsService(model_name)
        elif embeddings_type == "openai":
            if model_name == "":
                model_name = "text-embedding-3-small"
            return OpenAIEmbeddingsService(model_name)
        else:
            raise ValueError(f"Tipo de embeddings no soportado: {embeddings_type}")