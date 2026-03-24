from fastapi import APIRouter
from infraestructure.supabase import test_conection_db
from agents.chatbot_agent import get_test_agent, get_response_from_agent
from services.agent_service import vectordb_service
router = APIRouter(tags=["PRUEBA DE SERVICIOS"])


    
@router.get("/test-agent", description="Prueba el agente con una consulta de ejemplo.")
def test_agent():
    response = get_test_agent()
    return {"agent_response": response}

@router.get("/test-db", description="Prueba la conexion con la base de datos")
def health_check():
    try:
        db_response = test_conection_db()
        return {"status": "ok", "db_time": db_response}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@router.get("/test-vectordb", description="Prueba la conexión con la base de datos vectorial.")
def test_vectordb():
    try:
        vectordb_response = vectordb_service.test_bd()
        return {"status": "ok", "vectordb_response": vectordb_response}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.get("/test-agent-rag", description="Prueba el agente RAG con una consulta de ejemplo.")
def test_agent_rag(message: str):
    response = get_response_from_agent(message)
    return {"agent_response": response}