import os
from dotenv import load_dotenv

def configurar_llms():
    load_dotenv()  # Carrega as variáveis de ambiente definidas no arquivo .env

    gemini_key = os.getenv("GEMINI_API_KEY")  # Recupera a chave da Gemini API
    openai_key = os.getenv("OPENAI_API_KEY")  # Recupera a chave da OpenAI API (opcional)

    if gemini_key:
        # Define a variável de ambiente para uso interno na aplicação
        os.environ["GEMINI_API_KEY"] = gemini_key
    else:
        # Lança erro se a chave da Gemini não estiver presente 
        raise EnvironmentError("Variável GEMINI_API_KEY não encontrada no .env")

    if openai_key:
        # Define a variável de ambiente para OpenAI se estiver presente
        os.environ["OPENAI_API_KEY"] = openai_key
    else:
        # Remove a variável caso não tenha sido definida (evita conflito)
        os.environ.pop("OPENAI_API_KEY", None)

    # Define o provedor de LLM a ser usado pela CrewAI
    os.environ["CREWAI_LLM_PROVIDER"] = "gemini"
