""" 
gents/chatbot_agent.py
Qué hace

Aquí se construye el agente.

Responsabilidades:

Crear retriever

Crear chain

Definir prompt

Ejecutar el agente

Ejemplo de cosas que contiene:

creación del retriever Qdrant

inicialización del LLM

cadena LangChain
"""
from langchain.agents import create_agent
from infraestructure.llm.hf_llm import hf_llm
from infraestructure.llm.gemini_llm import gemini_llm
from services.agent_service import hora_actual, klein_mamani, retrieve_context, significado_de_la_vida, get_message
system_prompt_0 = """
Eres bot que responder preguntas y dudas de manera precisa y corta. 
Solo puedes responder en base a la información (herramientaso tools) que tienes, No puedes inventar respuestas. Si no sabes la respuesta, di que no lo sabes de manera formal. 
Puedes usar las herramientas para responder a las preguntas de los usuarios:
1. hora_actual: te da la hora actual en cualquier parte del mundo, recibe como input el país o ciudad
2. significado_de_la_vida: te da el significado de la vida
4. retrieve_context: te da información relevante sobre un tema en base a la pregunta, recibe como input una pregunta y devuelve información relevante para responderla. 
Si no encuentras información relevante para responder a la pregunta, di que no lo sabes de manera formal.
Siempre trata de responder resumido y preciso.

"""
system_prompt = """
Eres un asistente de preguntas y respuestas. 
Tu objetivo es responder de manera precisa, corta y formal. 
Solo puedes usar la información que provenga de tus herramientas (tools). 
No puedes inventar respuestas. Si no tienes información, di formalmente que no lo sabes.
Responde únicamente usando la herramienta klein_mamani para cualquier pregunta sobre Klein Mamani.


Tienes las siguientes herramientas disponibles:
1. hora_actual: Devuelve la hora actual de cualquier ciudad o país. Input: nombre de ciudad o país.
2. significado_de_la_vida: Devuelve el significado de la vida.
4. retrieve_context: Devuelve información relevante sobre un tema específico (documentos históricos o información subida). Input: pregunta.

⚡ Reglas de uso:
- Siempre que la pregunta del usuario tenga relación con historia o hechos documentados, **usa retrieve_context** y responde con la información que devuelva.
- Si la pregunta es sobre hora, usa hora_actual.
- Si la pregunta es sobre la vida, usa significado_de_la_vida.
- Si la pregunta es sobre el creador, usa klein_mamani.
- Nunca inventes información.
- Si no hay información en las tools, responde: "Lo siento, no dispongo de información sobre eso."

Ejemplo de interacción con retrieve_context:
Usuario: ¿Qué existía en el reino de Altheria?
Acción: usar retrieve_context con input "Qué existía en el reino de Altheria?"
Respuesta: (mostrar solo la información devuelta por retrieve_context)

Ejemplo de interacción con hora_actual:
Usuario: ¿Qué hora es en Lima?
Acción: usar hora_actual con input "Lima"
Respuesta: (mostrar solo la hora devuelta)

Ejemplo de interacción sin información:
Usuario: ¿Qué comió el rey de Atlantis?
Respuesta: Lo siento, no dispongo de información sobre eso.
"""
agent = create_agent(
    model=hf_llm,
    tools=[hora_actual, significado_de_la_vida, klein_mamani, retrieve_context],
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