from pydantic import BaseModel

# Define o modelo de resposta para a API utilizando Pydantic
class ArtigoResponse(BaseModel):
    tema: str   # Campo que armazena o tema do artigo
    artigo: str # Campo que armazena o conteúdo gerado do artigo
