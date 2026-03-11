from fastapi import APIRouter, Request
from services.message_service import reply_message

router = APIRouter(prefix="/twilio", tags=["Twilio Webhook"])


@router.post("/webhook")
async def webhook_handler(request: Request):
    form_data = await request.form()
    body = dict(form_data)
    try:
        reply_message(body, service="twilio")
    except Exception as e:
        print("Error:", e)
    
    