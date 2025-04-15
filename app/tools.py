from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests

# Modelo de entrada validado com Pydantic para garantir que a ferramenta receba uma consulta
class WikipediaInput(BaseModel):
    query: str = Field(..., description="Tema a ser pesquisado na Wikipedia")

# Ferramenta personalizada que busca informações na Wikipedia em português
class WikipediaTool(BaseTool):
    name: str = "WikipediaTool"  # Nome da ferramenta
    description: str = "Busca dados da Wikipedia em português."  # Descrição da funcionalidade

    # Método interno chamado para executar a ferramenta com o dado de entrada
    def _run(self, input_data: WikipediaInput) -> str:
        url = "https://pt.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "prop": "extracts",         # Solicita o texto dos artigos
            "exlimit": 1,
            "explaintext": 1,           # Retorna o texto puro
            "titles": input_data.query, # Tema pesquisado
            "format": "json",
            "utf8": 1,
            "redirects": 1              # Redireciona automaticamente se o termo tiver outro nome
        }
        try:
            # Requisição à API da Wikipedia
            resp = requests.get(url, params=params).json()
            # Acessa o conteúdo retornado e extrai o texto principal do artigo
            for page in resp.get("query", {}).get("pages", {}).values():
                return page.get("extract", "Informação não encontrada.")
        except Exception as e:
            return f"Erro: {e}"  # Retorna o erro caso ocorra falha na requisição
