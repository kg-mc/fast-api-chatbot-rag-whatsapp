from fastapi import APIRouter, Request, HTTPException
from services.meta_wsp_services import config_webhook
from services.message_service import reply_message
from utils import safe_get_str
from models.schemas import MessageSchema
router = APIRouter(prefix="/twilio", tags=["Twilio Webhook"])


@router.post("/webhook")
async def webhook_handler(request: Request):
    form_data = await request.form()
    body = dict(form_data)
    
    message_content = MessageSchema(**{
        "profile_name": safe_get_str(body.get("ProfileName")),
        "message_from": safe_get_str(body.get("From")),
        "body": body.get("Body")
    })
    print(message_content)
    if not all([message_content.profile_name, message_content.message_from, message_content.body]):
        raise HTTPException(status_code=400, detail="Faltan campos requeridos")
    response = reply_message(message_content=message_content, service="twilio")
    
    
    