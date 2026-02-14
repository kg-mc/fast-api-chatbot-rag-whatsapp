from datetime import datetime

from infraestructure.embbedings.embbedings import embed_query
from infraestructure.qdrant import search_in_qdrant
from langchain.tools import tool


## PRUEBAS

@tool("hora_actual", description="Usa esta herramienta cuando el usuario pregunte la hora local (Perú), fecha actual o qué hora es en Perú.")
def hora_actual() -> str:
    """Usa esta herramienta cuando el usuario pregunte la hora actual, fecha actual o qué hora es en Perú."""
    return datetime.now().strftime("%d/%m/%Y %H:%M")

@tool("significado_de_la_vida", description="Usa esta herramienta cuando el usuario pregunte por el significado de la vida.")
def significado_de_la_vida() -> str:
    """Usa esta herramienta cuando el usuario pregunte por el significado de la vida."""
    return "El significado de la vida es 42."   

@tool("retrieve_context", description="Usa esta herramienta para obtener contexto relevante para responder a la consulta del usuario.")
def retrieve_context(user_query: str) -> str:
    """Usa esta herramienta para obtener contexto relevante para responder a la consulta del usuario."""
    query_vector = embed_query(user_query).tolist()

    results = search_in_qdrant(query_vector)
    print("Resultados QDRANT ", results)
    texts = []

    for point in results:
        if point.payload and "text" in point.payload:
            texts.append(point.payload["text"])

    return "\n\n".join(texts)



###
# Funcion para generar un estandar de respuesta de llm (debido a que cada llm presentaba un formato diferente)
###
def get_message(response, model="hf_llm"):
    last_message = response["messages"][-1]
    messages = response["messages"]
    text_output = ""
    tools_used = []
    if model == "hf_llm":
        text_output = last_message.content if isinstance(last_message.content, str) else ""
        tools_used = []
        for msg in messages:
            tool_calls = getattr(msg, "tool_calls", None)
            if tool_calls:
                tools_used.extend(tool_calls)
    elif model == "gemini_llm":
        text_output = ""
        if isinstance(last_message.content, list):
            text_output = " ".join([c['text'] for c in last_message.content if c['type'] == 'text'])
        else:
            text_output = str(last_message.content)

        tools_used = []
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            tools_used = [call.name for call in last_message.tool_calls]
    
    return {
        "content": text_output, 
        "tool_calls": tools_used
    }