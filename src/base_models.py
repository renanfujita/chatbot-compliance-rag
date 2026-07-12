from pydantic import BaseModel, Field
from typing import Literal, List, Optional, TypedDict

# Modelo Pydantic para validação estruturada do LLM
class TriagemOut(BaseModel):
    decisao: Literal["AUTO_RESOLVER", "PEDIR_INFO", "ABRIR_CHAMADO"]
    urgencia: Literal["BAIXA", "MEDIA", "ALTA"]
    campos_faltantes: List[str] = Field(default_factory=list)


class AgentState(TypedDict, total=False):
    pergunta: str
    mensagem: str
    triagem: dict
    resposta: Optional[str]
    citacoes: list
    rag_sucesso: bool
    acao_final: str