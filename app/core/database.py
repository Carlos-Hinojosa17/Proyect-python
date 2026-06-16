from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Construir la URL de conexión a la base de datos
DATABASE_URL = (
    f"mysql+pymysql://"
    f"{settings.db_user}:"
    f"{settings.db_password}@"
    f"{settings.db_host}:"
    f"{settings.db_port}/"
    f"{settings.db_name}"
)

# Crear el motor de la base de datos
engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True
)

# Crear la sesión local para interactuar con la base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Crear la clase base para los modelos de SQLAlchemy
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()