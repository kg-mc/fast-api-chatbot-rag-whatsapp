from abc import ABC, abstractmethod
from typing import Optional
from infraestructure.twilio import client as twilio_client
from config import TWILIO_PHONE_NUMBER

class MessageService(ABC):

    @abstractmethod
    def send_message(self, to: str, message: str) -> str:
        pass


class TwilioService(MessageService):
    
    def send_message(self, to: str, message: str) -> Optional[str]:
        
        message_created = twilio_client.messages.create(
            body=message,
            from_=f"whatsapp:{TWILIO_PHONE_NUMBER}",
            to=to
        )
        #print(f"Mensaje enviado a {to} desde {TWILIO_PHONE_NUMBER}, mensaje: {message} con SID: {message_created.sid}")
        return message_created.sid
        
class MetaService(MessageService):

    def send_message(self, to: str, message: str):
        pass
    
    
class MessageServiceFactory:

    @staticmethod
    def create(service_type: str) -> MessageService:

        if service_type == "twilio":
            return TwilioService()

        elif service_type == "meta":
            return MetaService()

        else:
            raise ValueError("Servicio no soportado")
