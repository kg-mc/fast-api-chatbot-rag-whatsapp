
from google.genai import Client
import torch

# Inicializa el cliente de Gemini
client = Client()

def embed_query(query: str) -> torch.Tensor:
    # Usa el modelo de Gemini para generar un embedding
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query
    )
    
    if not response.embeddings:
        # Si no hay embeddings, lanza un error o retorna vector vacío
        raise ValueError("No se generó embedding para la query")
    
    # Toma el primer embedding y conviértelo a tensor
    embedding_vector = torch.tensor(response.embeddings[0].values)
    
    return embedding_vector