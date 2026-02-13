
from google.genai import Client
import torch

client = Client()

def embed_query(query: str) -> torch.Tensor:
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query
    )
    
    if not response.embeddings:
        raise ValueError("No se generó embedding para la query")
    
    embedding_vector = torch.tensor(response.embeddings[0].values)
    
    return embedding_vector