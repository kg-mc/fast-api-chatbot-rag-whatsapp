from fastapi import APIRouter, Request, HTTPException
from services.meta_wsp_services import config_webhook
router = APIRouter( tags=["Meta Webhook"])
### Aun falta desarrollar

@router.post("/webhook/")
def webhook_handler(message: str):
    return {
        "status": "Webhook received",
        "message": message
    }
    
@router.get("/webhook/")
def webhook_get(request: Request):
    query_params = request.query_params

    hub_mode = query_params.get("hub.mode")
    hub_challenge = query_params.get("hub.challenge")
    hub_verify_token = query_params.get("hub.verify_token")
    if not hub_mode or not hub_challenge or not hub_verify_token:
        raise HTTPException(status_code=400, detail="Falta parametros en la solicitud")
    
    return config_webhook(hub_mode, hub_challenge, hub_verify_token)