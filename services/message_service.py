from factory.message_factory import MessageServiceFactory
from agents.chatbot_agent import get_response_from_agent_w_history
from typing import Optional

sessions = {}

def reply_message(message_content, service: str) -> Optional[str]:
    message_service = MessageServiceFactory.create(service) 
    
    if message_service.extract_message_content(message_content):
        history = get_history(message_service.get_message_from())
        response = get_response_from_agent_w_history(message=message_service.get_message_content(), history=history)
        #asyncio.create_task(message_service.user_message())
        
        #print("Respuesta del agente: ", response["content"])
        _response = message_service.send_message( message=response["content"])
        save_message(user_id=message_service.get_message_from(), role="user", content=message_service.get_message_content())
        save_message(user_id=message_service.get_message_from(), role="assistant", content=response["content"])
        #print(get_history(message_service.get_message_from()))
    


def get_history(user_id):
    return sessions.get(user_id, [])

def save_message(user_id, role, content):
    if user_id not in sessions:
        sessions[user_id] = []

    sessions[user_id].append({
        "role": role,
        "content": content
    })

    # limitar memoria
    sessions[user_id] = sessions[user_id][-6:]