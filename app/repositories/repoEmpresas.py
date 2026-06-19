from sqlalchemy import Session
from app.models.empresas import empresas

class RepoEmpresas:
    def __init__(self, db: Session):
        self.db = db
    
    def create_empresa(self, empresa: empresas):
        self.db.add(empresa)
        self.db.commit()
        self.db.refresh(empresa)
        return empresa
    
    def get_empresa_by_id(self, id: int):
        return(
            self.db.query(empresas)
            .filter(empresas.id == id)
            .first()
        )
    
    def get_empresa_by_ruc(self, ruc: int):
        return(
            self.db.query(empresas)
            .filter(empresas.ruc == ruc)
            .first()
        )
    
    def get_all_empresas(self):
        return self.db.query(empresas).all()
        