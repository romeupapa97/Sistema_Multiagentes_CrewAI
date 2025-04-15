SISTEMA MULTIAGENTES COM CrewAI, Flask e Tkinter

Este projeto demonstra um sistema multiagentes utilizando [CrewAI](https://docs.crewai.com), com três agentes colaborativos(Consultor, Redator e Editor ) que geram um artigo científico com base em uma consulta à Wikipedia.



TECNOLOGIAS UTILIZADAS:

- CrewAI (multiagentes com LLMs)
- Flask (API backend)
- Tkinter (interface gráfica)
- Pydantic (validação de resposta)
- Gemini API (LLM principal)
- OpenAI (opcional, mas necessário para evitar fallback)


ESTRUTURA DO PROJETO

sistema_multiagente_crewai/
├── app/
|   ├── __init__.py    -->Torna o diretório um pacote Python
│   ├── agentes.py     --> agentes CrewAI
│   ├── crew.py        -->Execução da Crew
│   ├── llm_config.py  -->Configuração das chaves
│   ├── main.py        -->Flask API
│   ├── schemas.py     -->Respostas com pydantic
│   ├── tasks.py       -->Tarefas da Crew
│   └── tools.py       -->Personalização de wikipediaTool
├── interface/
│   └── gui.py         -->Interface Tkinter
├── requirements.txt 
├── README.md
├── .env               -->Arquivo de variáveis de ambiente (não incluído)


COMO EXECUTAR?

1. Crie o ambiente virtual

No terminal do VC code( estando na raiz do projeto).

com comandos:
'python -m venv venv'
e '.\venv\Scripts\activate'

O prompt mudará para algo como: (venv) PS C:\...>


2. Instale as dependências
'
'pip install -r requirements.txt'

3. Configure suas chaves de API
  Crie o arquivo '.env' no diretório do projeto com o seguinte conteúdo:
  GEMINI_API_KEY='sua chave gemini aqui'
  OPENAI_API_KEY='sua chave openai aqui' -->opcional, mas importante para evitar erros relacionados a OpenaAI.

4. Execute o servidor Flask (backend)
  Com comando: 'python -m app.main'
  depois de executar o API será iniciado.

5. Execute a interface gráfica com Tkinter
  Abra um novo terminal (com o ambiente virtual ainda ativo) e rode:
  'python interface/gui.py'

6. Teste

  Digite um tema (ex: LMM) na interface gráfica, clique em "Gerar Artigo", e o artigo completo será exibido no campo de texto.


OBSERVAÇÃO 1
  Recomenda-se fortemente o uso do Python 3.11.

  Durante o desenvolvimento deste projeto, enfrentei diversos erros ao tentar rodar o sistema com as versões 3.9, 3.10 e 3.12 do Python. Esses mesmos problemas também foram relatados por vários membros da comunidade CrewAI. Portanto, para evitar incompatibilidades e falhas de execução, recomenda-se fortemente utilizar Python 3.11.

OBSERVAÇÃO 2
  Durante o desenvolvimento, foi necessário utilizar a API da OpenAI como modelo de suporte. Isso ocorreu porque, ao utilizar apenas outros LLMs (como Gemini, Groq e outros), o sistema apresentava erros relacionados à ausência de implementação completa na biblioteca litellm, como: OpenAIError: ...

  Esse erro indica que o sistema, apesar de configurado para usar outros modelos, tentava acessar funcionalidades específicas da OpenAI, provavelmente por dependências internas do framework CrewAI ou por falta de suporte total da ferramenta alternativa utilizada.

  Assim, a chave da OpenAI foi fornecida de forma opcional no código para garantir compatibilidade e estabilidade na execução das tarefas. 

Pode não acontecer com você o mesmo problema que eu tive, mas eu achei importante avisar.