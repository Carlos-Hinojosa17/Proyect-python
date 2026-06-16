from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Configuración de la base de datos
    db_host: str
    db_port: int
    db_user: str
    db_password: str

    db_name: str
    # Configuración para cargar las variables de entorno desde el archivo .env
    class Config:
        env_file = ".env"

settings = Settings()