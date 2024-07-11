# Just another to-do list

Este projeto é um exemplo para treinar conceitos básicos de criação de uma API.

#### Conceitos Trabalhados
- **Gerenciamento de Pacotes e Ambiente:**
  - Utiliza [Poetry](https://python-poetry.org/) para gerenciamento de dependências.
  - Configuração do ambiente com [Pyenv](https://github.com/pyenv/pyenv) para controle de versões Python.
  - Uso do [pipx](https://pipx.pypa.io/stable/installation/) para instalação de ferramentas Python de forma isolada.

- **Boas Práticas de Desenvolvimento:**
  - Desenvolvimento orientado por testes (TDD).

- **API:**
  - Implementação da API usando [FastAPI](https://fastapi.tiangolo.com/).
  - Utilização do padrão OpenAPI para documentação ([link para mais informações sobre o OpenAPI](https://www.openapis.org/)).

- **Autenticação e Autorização:**
  - Implementação de autenticação JWT para segurança.
  - Autorização baseada em permissões.

- **Modelagem de Dados:**
  - Utilização de [Pydantic](https://docs.pydantic.dev/latest/) para validação de dados.
  - Persistência de dados com [SQLAlchemy](https://www.sqlalchemy.org/).

#### Pré-Requisitos
- Git para versionamento do código.
- Pyenv para gerenciamento de versões Python (recomendada versão 3.12.*).
- Poetry para gerenciamento de pacotes de dependências.

#### Setup
Para começar a usar o projeto:

1. **Clonar o Repositório:**
   ```bash
   git clone git@github.com:pcastr/jatlist.git
   cd jatlist/jatlist_api
   ```

2. **Configuração do Ambiente:**
   ```bash
   poetry config virtualenvs.in-project true
   poetry config virtualenvs.prefer-active-python true
   poetry install --no-root
   poetry shell
   ```
3. **Inserir variáveis de ambiente do arquivo .env_example**
   ```
   mv .env_example  .env

   nano .env # inserir variáveis de ambiente
    # Dependendo do banco ultizado pode ser nescessário configuração do alembic
   ```
4. **Executar o Projeto:**
   - Ativar o servidor:
     ```bash
     task run
     ```
     Acesse a documentação em: [http://localhost:8000/docs](http://localhost:8000/docs).

   - Rodar os testes:
     ```bash
     task test
     ```
