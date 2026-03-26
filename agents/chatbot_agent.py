from langchain.agents import create_agent
from services.agent_service import hora_actual, retrieve_context, saludo, get_message, about_cader, about_me, eje_tematico, lugar_cader, fecha_cader, no_se, servicios_taxi
from config import system_prompt_0, llm_model
from factory.llm_factory import LLMFactory

llm_service = LLMFactory.create_llm_service(llm_type=llm_model)
llm = llm_service.get_llm()


agent = create_agent(
    model=llm,
    tools=[hora_actual, retrieve_context, eje_tematico, saludo, lugar_cader, fecha_cader, about_me, about_cader, no_se, servicios_taxi],
    system_prompt=system_prompt_0
)

def get_test_agent():
    response = agent.invoke({
        "messages": [
            {
                "role": "user", 
                "content": "Dime la hora actual en Perú"
             }
        ]
    })
    return response

def get_response_from_agent(message: str):
    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    })
    #print(response)
    #last_message = response["messages"][-1]
    
    #message_data = get_message(response, model=llm_model)
    message_data = llm_service.get_message(response)

    return message_data

def get_response_from_agent_w_history(message: str, history):
    response = agent.invoke({
        "messages": history + [
            {
                "role": "user",
                "content": message
            }
        ]
    })
    #print(response)
    #last_message = response["messages"][-1]
    
    #message_data = get_message(response, model=llm_model)
    message_data = llm_service.get_message(response)
    return message_data