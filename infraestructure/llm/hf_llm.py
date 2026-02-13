from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from config import TOKEN_HF

llm_endpoint = HuggingFaceEndpoint(
    model="openai/gpt-oss-120b",
    huggingfacehub_api_token=TOKEN_HF,
    temperature=0,
    max_new_tokens=500,
)

hf_llm = ChatHuggingFace(llm=llm_endpoint)


