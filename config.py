from dotenv import load_dotenv
import os


load_dotenv()


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