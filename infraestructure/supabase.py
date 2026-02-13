
import psycopg2
from config import USER_DB, PASSWORD_DB, HOST_DB, PORT_DB, NAME_DB

connection = psycopg2.connect(
            user=USER_DB,
            password=PASSWORD_DB,
            host=HOST_DB,
            port=PORT_DB,
            dbname=NAME_DB
        )

def test_conection_db():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        cursor.close()
        return result
    except Exception as e:
        return f"Error al conectar a la base de datos: {e}"