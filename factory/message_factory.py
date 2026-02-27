from abc import ABC, abstractmethod
from typing import Optional

import requests
from infraestructure.twilio import client as twilio_client
from config import TWILIO_PHONE_NUMBER, META_ACCESS_TOKEN, META_PHONE_NUMBER_ID
from models.schemas import MessageSchema
from services.user_service import user_exists, add_user
from utils import safe_get_str


class MessageService(ABC):
    message_content: MessageSchema 
    async def user_message(self, profile_name: str):
        if not await user_exists(profile_name):
            await add_user(profile_name)
            print(f"Nuevo usuario agregado: {profile_name}")
    def get_message_content(self):
        return self.message_content.body
    @abstractmethod
    def send_message(self, message: str) -> Optional[str]:
        pass
    @abstractmethod
    def extract_message_content(self, body):
        pass


class TwilioService(MessageService):
    
    def send_message(self, message: str) -> Optional[str]:
        
        message_created = twilio_client.messages.create(
            body=message,
            from_=f"whatsapp:{TWILIO_PHONE_NUMBER}",
            to=self.message_content.message_from
        )
        #print(f"Mensaje enviado a {to} desde {TWILIO_PHONE_NUMBER}, mensaje: {message} con SID: {message_created.sid}")
        return message_created.sid
    def extract_message_content(self, body):
        try:
            
            self.message_content = MessageSchema(**{
                "profile_name": safe_get_str(body.get("ProfileName")),
                "message_from": safe_get_str(body.get("From")),
                "body": body.get("Body")
            })
            return True
        except Exception as e:
            print(f"Error al extraer contenido del mensaje de Twilio: {e}")
            return False
        
        
class MetaService(MessageService):
    
    def send_message(self, message: str) -> Optional[str]:
        headers = {
            "Authorization": f"Bearer {META_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": self.message_content.message_from,
            "type": "text",
            "text": {
                "body": message
            }
        }
        try:
            response = requests.post(f"https://graph.facebook.com/v22.0/{META_PHONE_NUMBER_ID}/messages", headers=headers, json=payload)
            if response.status_code == 200:
                #print(f"Mensaje enviado a {self.message_content.message_from} a través de Meta, mensaje: {message}")
                return response.json().get("message_id")
        except Exception as e:
            print(f"Error al enviar mensaje a través de Meta: {e}")
            return None
    def extract_message_content(self, body):
        value = body.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {})

        #solo para responder y extraer informacion cuando sea un mensaje verdadero, no para eventos de mensajes eliminados o editados
        if "messages" not in value:
            return False

        try:
            profile_name = value.get("contacts", [{}])[0].get("profile", {}).get("name")
            from_number = value.get("messages", [{}])[0].get("from")
            message_body = value.get("messages", [{}])[0].get("text", {}).get("body")

            self.message_content = MessageSchema(**{
                "profile_name": profile_name,
                "message_from": from_number,
                "body": message_body
            })
            return True

        except Exception as e:
            print(f"Error al extraer contenido del mensaje de Meta: {e}")
            return False
        
    
    
class MessageServiceFactory:

    @staticmethod
    def create(service_type: str) -> MessageService:

        if service_type == "twilio":
            return TwilioService()

        elif service_type == "meta":
            return MetaService()

        else:
            raise ValueError("Servicio no soportado")
