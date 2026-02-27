from factory.message_factory import MessageService
from factory.message_factory import MessageServiceFactory
from models.schemas import MessageSchema
from agents.chatbot_agent import get_response_from_agent
from typing import Optional
import asyncio

def save_message(user: int, message: str):
    # human and ia 
    pass


def reply_message(message_content, service: str) -> Optional[str]:
    message_service = MessageServiceFactory.create(service) 
    
    if message_service.extract_message_content(message_content):
        response = get_response_from_agent(message=message_service.get_message_content())
        #asyncio.create_task(message_service.user_message())
        #print("Respuesta del agente: ", response["content"])
        response = message_service.send_message( message=response["content"])
    
    
