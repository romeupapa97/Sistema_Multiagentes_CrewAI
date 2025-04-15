from flask import Flask, request, jsonify
from app.crew import executar_crew
from app.schemas import ArtigoResponse
from app.llm_config import configurar_llms

app = Flask(__name__)  # Cria a instância da aplicação Flask
configurar_llms()      # Carrega as variáveis de ambiente necessárias para os LLMs

@app.route("/gerar_artigo", methods=["POST"])
def gerar_artigo():
    data = request.get_json()         # Recebe o JSON enviado na requisição
    tema = data.get("tema")           # Extrai o tema informado pelo usuário

    if not tema:
        return jsonify({"erro": "Informe o tema."}), 400  # Retorna erro se o tema estiver vazio

    artigo = executar_crew(tema)      # Executa a Crew com base no tema fornecido
    resposta = ArtigoResponse(tema=tema, artigo=artigo.raw)  # Cria objeto de resposta usando o modelo Pydantic
    return jsonify(resposta.dict())   # Retorna o artigo em formato JSON

if __name__ == "__main__":
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração
