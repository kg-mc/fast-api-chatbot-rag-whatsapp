from langchain.agents import create_agent
from infraestructure.llm.hf_llm import hf_llm
from infraestructure.llm.gemini_llm import gemini_llm
from services.agent_service import hora_actual, retrieve_context, significado_de_la_vida, get_message
from config import system_prompt_0

agent = create_agent(
    model=hf_llm,
    tools=[hora_actual, significado_de_la_vida, retrieve_context],
    system_prompt=system_prompt_0
)

def get_test_agent():
    response = agent.invoke({
        "messages": [
            {
                "role": "user", 
                "content": "Dime la hora a  ctual en Perú"
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
    print(response)
    #last_message = response["messages"][-1]
    
    message_data = get_message(response, model="hf_llm")

    return message_data