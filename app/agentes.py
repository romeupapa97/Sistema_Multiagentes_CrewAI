# Importa a classe Agent da biblioteca CrewAI, usada para criar agentes autônomos com comportamentos definidos.
from crewai import Agent
# Importa a ferramenta personalizada que faz consultas à Wikipedia.
from app.tools import WikipediaTool

# Instancia a ferramenta da Wikipedia, que será usada pelo consultor.
wiki_tool = WikipediaTool()

# Define o agente "Consultor", responsável por buscar informações na Wikipedia.
consultor = Agent(
    role='Consultor da informação',  # Papel do agente dentro da equipe
    goal='Buscar dados da Wikipedia sobre um tema',  # Objetivo principal da sua atuação
    backstory='Você é um consultor especialista em dados enciclopédicos.',  # Contexto que orienta o comportamento do agente
    ttools=[wiki_tool],  # Ferramenta disponível para o agente, neste caso, apenas Wikipedia
    verbose=True  # Exibe os logs detalhados durante a execução
)

# Define o agente "Redator", responsável por escrever um artigo com base nas informações coletadas.
redator = Agent(
    role='Redator científico',
    goal='Escrever artigo acadêmico com pelo menos 300 palavras',
    backstory='Você transforma informação em textos científicos.',
    verbose=True
)

# Define o agente "Editor", responsável por revisar e refinar o texto gerado.
editor = Agent(
    role='Editor acadêmico',
    goal='Revisar e melhorar a linguagem acadêmica do artigo',
    backstory='Você corrige e aprimora o texto final.',
    verbose=True
)
