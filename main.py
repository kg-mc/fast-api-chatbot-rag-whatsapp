from fastapi import FastAPI
#from api.whatsapp_meta_router import router as meta_router
from api.tests_services_router import router as tests_router
from api.twilio_router import router as twilio_router
#
app = FastAPI(redirect_slashes=False)

#app.include_router(meta_router)
app.include_router(tests_router)
app.include_router(twilio_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
