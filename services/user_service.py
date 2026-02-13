"""
AQUI SE GESTIONARAN USUARIOS CON SUPABASE, VALIDAR SI EXISTEN, AGREGAR USUARIO A LA BD
"""

"""

## POR DESARROLLAR
""" 
from infraestructure.supabase import connection

async def user_exists(user: int) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM users WHERE id = %s;", (1,))
        result = cursor.fetchone()
        cursor.close()
        return result is not None
    except Exception as e:
        print(f"Error al validar existencia del usuario: {e}")
        return True