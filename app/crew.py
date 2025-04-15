from crewai import Crew  # Classe principal para coordenar os agentes e suas tarefas
from app.tasks import consulta_tarefa, redacao_tarefa, edicao_tarefa  # Importa as tarefas que serão executadas

def executar_crew(tema: str) -> str:
    # Personaliza a descrição das tarefas com o tema fornecido pelo usuário
    consulta_tarefa.description = consulta_tarefa.description.format(tema=tema)
    redacao_tarefa.description = redacao_tarefa.description.format(tema=tema)

    # Cria a equipe com os agentes e suas respectivas tarefas
    equipe = Crew(
        agents=[consulta_tarefa.agent, redacao_tarefa.agent, edicao_tarefa.agent],
        tasks=[consulta_tarefa, redacao_tarefa, edicao_tarefa],
        verbose=True  # Habilita logs detalhados da execução
    )

    # Executa a equipe passando o tema como input inicial
    return equipe.kickoff(inputs={"tema": tema})
