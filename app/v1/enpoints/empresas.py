from fastapi import APIRouter, Depends
from schemas.schEmpresasRespons import SchemaEmpresaResponse
from services.servEmpresas import ServEmpresas
from repositories.repoEmpresas import RepoEmpresas
from models.empresas import Empresa

router = APIRouter()

@router.post(
    "/",
    response_model=SchemaEmpresaResponse
)
def create_empresa(
    empresa: CreateEmpresa,
    db: Session = Depends(get_db)
):
    repo = RepoEmpresas(db)

    service = ServEmpresas(repo)

    return service.create_empresa(
        Empresa(**empresa.model_dump())
    )