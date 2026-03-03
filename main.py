from fastapi import FastAPI
from api.whatsapp_meta_router import router as meta_router
from api.tests_services_router import router as tests_router
from api.twilio_router import router as twilio_router
from contextlib import asynccontextmanager

#
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("\n" + "="*40)
    print("🚀 CONFIGURACIONES DEL BOT DE WHATSAPP")
    print("="*40)
    
    print(f"[+] Modelo de IA generativa: openai/gpt-oss-120b")
    print(f"[+] Modelo de embeddings: BAAI/bge-m3")
    print(f"[+] Base de datos: postgresql - Supabase")
    print(f"[+] Servicios de mensajería: Twilio y Meta (WhatsApp Business API)")
    print(f"[+] Vector database: Qdrant")
    print("="*40 + "\n")

    yield

    print("\n🛑 Apagando el bot y cerrando conexiones...")

app = FastAPI(redirect_slashes=False, lifespan=lifespan)


app.include_router(meta_router)
app.include_router(tests_router)
app.include_router(twilio_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
