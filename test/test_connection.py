from sqlalchemy import text
from app.core.database import engine

print("Inicio del script")
def test_db_connection():
    try:
        with engine.connect() as connection:
            db_name = connection.execute(text("SELECT DATABASE()")).scalar()
            print(f"Conexion exitosa a la base de datos: {db_name}")
    except Exception as e:
        print("No se pudo conectar a la base de datos: ")
        print("Error: ", str(e))
    
if __name__ == "__main__":
        test_db_connection()