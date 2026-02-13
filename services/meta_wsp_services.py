from fastapi import HTTPException
from fastapi.responses import PlainTextResponse

### AUN POR DESARROLLAR
VERIFY_TOKEN = "1158201444"
def config_webhook(hub_mode: str, hub_challenge: str, hub_verify_token: str):
    if hub_verify_token != VERIFY_TOKEN:
        raise HTTPException(status_code=403, detail="Token de verificacion invalido")

    if hub_mode == "subscribe":
        return PlainTextResponse(hub_challenge)
    else:
        raise HTTPException(status_code=400, detail="MODO NO EXISTENTE")