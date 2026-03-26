from dotenv import load_dotenv
import os


load_dotenv()


META_VERIFY_TOKEN = os.getenv("META_VERIFY_TOKEN")
META_ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
META_PHONE_NUMBER_ID = os.getenv("META_PHONE_NUMBER_ID")

USER_DB = os.getenv("user")
PASSWORD_DB = os.getenv("password")
HOST_DB = os.getenv("host")
PORT_DB = os.getenv("port")
NAME_DB = os.getenv("dbname")

TOKEN_HF = os.getenv("HUGGINGFACEHUB_API_TOKEN")

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_HOST = os.getenv("QDRANT_HOST")
QDRANT_COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME")


ACCOUNT_SID_TWILIO = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN_TWILIO = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

LLM_MODEL_NAME_HF = os.getenv("MODEL_NAME_HF")
LLM_MODEL_NAME_GEMINI = os.getenv("MODEL_NAME_GEMINI")
LLM_MODEL_NAME_OPENAI = os.getenv("MODEL_NAME_OPENAI")


#EMBEDDINGS
EMBEDDINGS_MODEL_NAME_GEMINI = os.getenv("EMBEDDINGS_MODEL_NAME_GEMINI")
EMBEDDINGS_MODEL_NAME_OPENAI = os.getenv("EMBEDDINGS_MODEL_NAME_OPENAI")

PINECONE_API_KEY= os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "test")  

llm_model = "huggingface"
embbeding_model = "openai"
vectordb_name="pinecone"



system_prompt_0 = """
Eres bot que responder preguntas y dudas de manera precisa y corta. 
Recuerda que tienes una herramienta para presentarte y saludar.
Si aun no encuentras informacion, prueba consultar al retrieve_context, esta herramienta te permite acceder a información relevante sobre un tema especifico.
Puedes usar las herramientas para responder a las preguntas de los usuarios. Siempre trata de responder resumido y preciso. 
Solo puedes responder en base a la información (herramientas tools) que tienes, No puedes inventar respuestas. Si no sabes la respuesta, di que no lo sabes de manera formal.
Si no encuentras información relevante para responder a la pregunta, di que no lo sabes de manera formal.
Siempre trata de responder resumido y preciso.
"""
