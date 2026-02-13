from factory.message_factory import MessageService
from factory.message_factory import MessageServiceFactory
from models.schemas import MessageSchema
from agents.chatbot_agent import get_response_from_agent

def save_message(user: int, message: str):
    pass


def reply_message(message_content: MessageSchema, service: str) -> str:
    message_service = MessageServiceFactory.create(service)
    response = get_response_from_agent(message=message_content.body)
    #print("Tools", response["tool_calls"], "Response content", response["content"])
    response = message_service.send_message(to=message_content.message_from, message=response["content"])
    return response
    
