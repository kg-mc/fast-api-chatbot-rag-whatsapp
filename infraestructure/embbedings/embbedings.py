from sentence_transformers import SentenceTransformer
from torch import Tensor

model = SentenceTransformer("BAAI/bge-m3")
#instruction = "Represent this question for retrieving relevant passages: "
instruction_2 = "Represent this question for retrieving supporting documents: "


def embed_query(query: str):
    embedding = model.encode(
        [instruction_2 + query],
        normalize_embeddings=True
    )
    return embedding[0]
    
# probando con gemini por ahora