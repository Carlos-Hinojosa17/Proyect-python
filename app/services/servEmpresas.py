from repositories.repoEmpresas import RepoEmpresas

class ServEmpresas:
    def __init__(self, repo: RepoEmpresas):
        self.repo = repo
    
    def create_empresa(self, empresa):
        return self.repo.create_empresa(empresa)
    
    def get_empresa_by_id(self, id: int):
        return self.repo.get_empresa_by_id(id)
    
    def get_empresa_by_ruc(self, ruc: int):
        return self.repo.get_empresa_by_ruc(ruc)
    
    def get_all_empresas(self):
        return self.repo.get_all_empresas()