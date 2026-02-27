"""
AQUI SE GESTIONARAN USUARIOS CON SUPABASE, VALIDAR SI EXISTEN, AGREGAR USUARIO A LA BD
"""

"""

## POR DESARROLLAR
""" 
from infraestructure.supabase import connection

async def user_exists(number_from: str) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM users WHERE phone_number = %s;", (number_from,))
        result = cursor.fetchone()
        cursor.close()
        return result is not None
    except Exception as e:
        print(f"Error al validar existencia del usuario: {e}")
        return False
    
async def add_user(phone_number: str) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (phone_number) VALUES (%s);", (phone_number,))
        connection.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error al agregar usuario: {phone_number}")
        return False