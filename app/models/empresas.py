from sqlalchemy import Column, Integer, String
from app.core.database import Base

class empresas(Base):
    __tablename__ ='tblempresas'
    id = Column(Integer, primary_key=True, index=True)
    ruc = Column(String(11), nullable=False, unique=True, index=True)
    razon = Column(String(255), nullable=False, index=True)
    departamento = Column(String(255), nullable=False)
    provincia = Column(String(255), nullable=False)
    distrito = Column(String(255), nullable=False)
    direccion = Column(String(255), nullable=False)
    representante = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
