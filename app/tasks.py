from crewai import Task
from app.agentes import consultor, redator, editor

# Tarefa atribuída ao consultor: buscar informações na Wikipedia
consulta_tarefa = Task(
    description="Busque e organize as informações mais relevantes sobre o tema '{tema}'.",
    agent=consultor,  # Agente responsável pela busca de dados
    expected_output="Texto com dados da Wikipedia."  # Resultado esperado da tarefa
)

# Tarefa atribuída ao redator: escrever o artigo com base nas informações coletadas
redacao_tarefa = Task(
    description="Com base nas informações, redija um artigo de no mínimo 300 palavras.",
    agent=redator,  # Agente responsável pela redação do conteúdo
    expected_output="Artigo com introdução, desenvolvimento e conclusão."
)

# Tarefa atribuída ao editor: revisar e aprimorar o texto do artigo
edicao_tarefa = Task(
    description="Revisar o artigo gerado para garantir clareza, tom acadêmico e fluidez.",
    agent=editor,  # Agente responsável pela revisão final
    expected_output="Artigo final revisado com parágrafos corridos e linguagem acadêmica."
)
