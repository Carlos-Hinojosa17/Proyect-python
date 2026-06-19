from pydantic import BaseModel
class schemaEmpresasRespons(BaseModel):
    id: int
    ruc: int
    razon: str
    departamento: str
    provincia: str
    distrito: str
    direccion: str
    representante: str
    telefono: str
    email: str

    class Config:
        from_attributes = True