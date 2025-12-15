# To-Do List API: Sistema CRUD Completo com Docker

## Descrição do Projeto

Backend RESTful desenvolvido em **Python** (FastAPI) e **SQLAlchemy**. Implementa operações CRUD completas (Criar, Ler, Atualizar, Excluir) para gerenciamento de tarefas, demonstrando proficiência em desenvolvimento de API de alta performance e persistência de dados relacional (SQLite).

O projeto atende aos requisitos de **Integração de API REST** e **Banco de Dados Relacional**, e inclui o diferencial de **Empacotamento com Docker**.

## Tecnologias e Bibliotecas Utilizadas

* **Linguagem:** Python 3.10+
* **Framework API:** FastAPI (Para a criação dos endpoints REST).
* **ORM/BD:** SQLAlchemy (Para manipulação de dados em SQL através de objetos Python).
* **Banco de Dados:** SQLite (Banco de dados relacional simples e local).
* **Contêineres:** Docker e Docker Compose (Para empacotamento e execução facilitada).
* **Servidor:** Uvicorn (Servidor ASGI para executar a aplicação FastAPI).
* **Validação:** Pydantic (Usado pelo FastAPI para tipagem e validação dos dados).

## 🚀 Como Rodar o Projeto

Você tem duas opções para rodar a aplicação: com Docker (recomendado) ou localmente.

### Opção 1: Rodar com Docker (Recomendado)

Esta é a maneira mais simples, pois não requer configuração do ambiente Python local.

#### Pré-requisitos
* **Docker Desktop** (ou Docker Engine) instalado.

#### Instruções
1.  **Clone o Repositório e Navegue:**
    ```bash
    git clone [https://github.com/erikhko/todo-list-api.git](https://github.com/erikhko/todo-list-api.git)
    cd todo-list-api
    ```

2.  **Construa e Inicie o Contêiner:**
    O Docker Compose fará o *build* da imagem e iniciará o servidor na porta 8000.
    ```bash
    docker compose up --build
    ```
    O servidor estará acessível em **http://localhost:8000**.

### Opção 2: Rodar Localmente (Ambiente Virtual)

#### Pré-requisitos
* Python 3.10+ e Git instalados.

#### Instruções
1.  **Clone o Repositório e Navegue:**
    ```bash
    git clone [https://github.com/erikhko/todo-list-api.git](https://github.com/erikhko/todo-list-api.git)
    cd todo-list-api
    ```

2.  **Configurar e Ativar o Ambiente Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/macOS/Git Bash
    # venv\Scripts\activate  # Para Windows CMD/PowerShell
    ```

3.  **Instalar Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Caso o arquivo `requirements.txt` não exista, use: `pip install fastapi "uvicorn[standard]" sqlalchemy pydantic`)*.

4.  **Iniciar a Aplicação:**
    ```bash
    uvicorn main:app --reload
    ```
    A API estará rodando no endereço **`http://127.0.0.1:8000`**.

## Teste e Documentação dos Endpoints

Você pode testar todos os endpoints diretamente através da documentação interativa (Swagger UI) fornecida pelo FastAPI:

Acesse: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

* `/tasks/` - **POST**: Cria uma nova tarefa.
* `/tasks/` - **GET**: Lista todas as tarefas (com suporte à paginação).
* `/tasks/{id}` - **GET**: Busca uma tarefa específica.
* `/tasks/{id}` - **PATCH**: Atualiza o título e/ou o status (`is_done`) da tarefa.
* `/tasks/{id}` - **DELETE**: Remove uma tarefa.

## Próximos Passos (Diferenciais Futuros)

O próximo foco de desenvolvimento será na integração de funcionalidades de Inteligência Artificial:

* **Integração de LLMs:** Desenvolvimento de um novo endpoint utilizando a API da OpenAI/LangChain.

## Licença

Este projeto está licenciado sob a Licença MIT.
Consulte o arquivo [LICENSE.txt](LICENSE.txt) para mais detalhes.
