from fastapi import APIRouter
from infraestructure.supabase import test_conection_db
from agents.chatbot_agent import get_test_agent
from infraestructure.qdrant import test_conection_qdrant

router = APIRouter(tags=["PRUEBA DE SERVICIOS"])


    
@router.get("/test-agent")
def test_agent():
    response = get_test_agent()
    return {"agent_response": response}

@router.get("/test-db")
def health_check():
    try:
        db_response = test_conection_db()
        return {"status": "ok", "db_time": db_response}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@router.get("/test-qdrant")
def test_qdrant():
    try:
        qdrant_response = test_conection_qdrant()
        return {"status": "ok", "qdrant_response": qdrant_response}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    