from fastapi import APIRouter, Request, HTTPException
from services.meta_wsp_services import config_webhook
from services.message_service import reply_message
from models.schemas import MessageSchema
router = APIRouter(prefix="/twilio", tags=["Twilio Webhook"])


@router.post("/webhook")
async def webhook_handler(request: Request):
    form_data = await request.form()
    body = dict(form_data)
    try:
        reply_message(body, service="twilio")
    except Exception as e:
        print("Error:", e)
    
    