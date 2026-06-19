from pydantic import BaseModel

class CreateEmpresas(BaseModel):
    ruc: int
    razon: str
    departamento: str
    provincia: str
    distrito: str
    direccion: str
    representante: str
    telefono: str
    email: str