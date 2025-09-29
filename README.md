# 📌 Customers API (FastAPI)
Uma API REST moderna para **gerenciamento de clientes**, desenvolvida em Python utilizando **FastAPI** e **SQLAlchemy**.
Este projeto foi desenvolvido como case técnico e oferece flexibilidade de execução tanto em ambiente containerizado com **Docker + PostgreSQL** quanto localmente utilizando **SQLite**.
---
## 📚 Índice
- [🚀 Tecnologias utilizadas](#-tecnologias-utilizadas)
- [📂 Estrutura de pastas](#-estrutura-de-pastas)
- [⚙️ Como rodar o projeto](#️-como-rodar-o-projeto)
  - [1️⃣ Clonar o repositório](#1️⃣-clonar-o-repositório)
  - [2️⃣ Rodando com Docker + PostgreSQL](#2️⃣-rodando-com-docker--postgresql)
  - [3️⃣ Rodando sem Docker (SQLite local)](#3️⃣-rodando-sem-docker-sqlite-local)
- [📌 Endpoints principais](#-endpoints-principais)
- [🔍 Exemplos de chamadas](#-exemplos-de-chamadas)
- [🛠️ O que cada camada faz](#️-o-que-cada-camada-faz)
- [🧪 Testes](#-testes)
- [🔍 Testando manualmente](#-testando-manualmente)
- [📦 Docker Compose](#-docker-compose)
---
## 🚀 Tecnologias Utilizadas
- **Python 3.12+** - Linguagem de programação principal
- **FastAPI** - Framework web moderno e de alta performance
- **SQLAlchemy** - ORM robusto para persistência de dados
- **PostgreSQL** - Banco de dados relacional (ambiente Docker)
- **SQLite** - Banco de dados local para desenvolvimento rápido
- **pytest** - Framework para testes unitários e de integração
- **Uvicorn** - Servidor ASGI de alto desempenho
---
## 📂 Estrutura do Projeto
```text
app/
├── routers/       # Endpoints da API (controllers)
├── services/      # Lógica de negócio da aplicação
├── repositories/  # Camada de acesso aos dados
├── models/        # Modelos ORM (SQLAlchemy)
├── schemas/       # Schemas Pydantic para validação
├── db.py          # Configuração e conexão com banco de dados
├── main.py        # Arquivo principal da aplicação
└── tests/         # Testes unitários e de integração
```
---
## ⚙️ Como Executar o Projeto
### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/customers-api.git
cd customers-api
```
### 2️⃣ Executando com Docker + PostgreSQL
1. **Inicializar o container do banco de dados:**
   ```bash
   docker compose up -d db
   ```
2. **Criar ambiente virtual e instalar dependências:**
   ```bash
   python -m venv .venv
   
   # Windows
   .\.venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   
   pip install -r requirements.txt
   ```
3. **Configurar variável de ambiente para PostgreSQL:**
   ```bash
   # Windows
   set DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/customers
   
   # Linux/Mac
   export DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/customers
   ```
4. **Executar a API:**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
### 3️⃣ Executando Localmente com SQLite
```bash
# Criar ambiente virtual
python -m venv .venv
# Ativar ambiente virtual
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
# Instalar dependências
pip install -r requirements.txt
# Configurar para usar SQLite
# Windows
set USE_SQLITE=1
# Linux/Mac
export USE_SQLITE=1
# Executar a API
uvicorn app.main:app --reload --port 8000
```
---
## 📌 Endpoints da API
| Método | Endpoint           | Descrição                                    |
|--------|--------------------|--------------------------------------------|
| POST   | `/clientes`        | Cadastra um novo cliente                   |
| GET    | `/clientes`        | Lista todos os clientes cadastrados        |
| GET    | `/clientes/{id}`   | Consulta um cliente específico por ID      |
| GET    | `/clientes?nome=x` | Busca clientes que contenham o nome "x"    |
| GET    | `/health`          | Verificação de saúde da API                |
---
## 🔍 Exemplos de Uso da API
### Criar Cliente (POST `/clientes`)
**Requisição:**
```json
{
  "nome": "Lucas Silva",
  "email": "lucas@exemplo.com",
  "telefone": "11999990000"
}
```
### Listar Clientes (GET `/clientes`)
**Resposta:**
```json
[
  {
    "id": "5b15cd0d-ca81-4e3d-a2ca-43ecc267abea",
    "nome": "Lucas Silva",
    "email": "lucas@exemplo.com",
    "telefone": "11999990000",
    "created_at": "2025-09-28T23:35:13"
  },
  {
    "id": "33ac7357-3df5-4e3d-bea7-9810c41f0fa7",
    "nome": "Maria Silva",
    "email": "maria@exemplo.com",
    "telefone": "11999990000",
    "created_at": "2025-09-28T23:28:57"
  }
]
```
### Buscar por ID (GET `/clientes/{id}`)
**Resposta:**
```json
{
  "id": "5b15cd0d-ca81-4e3d-a2ca-43ecc267abea",
  "nome": "Lucas Silva",
  "email": "lucas@exemplo.com",
  "telefone": "11999990000",
  "created_at": "2025-09-28T23:35:13"
}
```
### Buscar por Nome (GET `/clientes?nome=Maria`)
**Resposta:**
```json
[
  {
    "id": "33ac7357-3df5-4e3d-bea7-9810c41f0fa7",
    "nome": "Maria Silva",
    "email": "maria@exemplo.com",
    "telefone": "11999990000",
    "created_at": "2025-09-28T23:28:57"
  }
]
```
---
## 🛠️ Arquitetura e Responsabilidades
A aplicação segue uma arquitetura em camadas bem definida:
- **Routers** - Define os endpoints da API e gerencia requisições HTTP
- **Services** - Concentra a lógica de negócio da aplicação
- **Repositories** - Responsável pelo acesso e manipulação de dados
- **Models** - Define as entidades e tabelas do banco de dados
- **Schemas** - Validação e serialização de dados (entrada/saída)
- **db.py** - Configuração e gerenciamento de conexões com banco
- **main.py** - Ponto de entrada e inicialização da aplicação
---
## 🧪 Testes Automatizados
Para executar todos os testes:
```bash
pytest -v
```
### Cobertura de Testes
Os testes implementados cobrem:
- ✅ Cadastro de cliente válido
- ✅ Validação de e-mail duplicado
- ✅ Listagem completa de clientes
- ✅ Busca por nome (filtro)
- ✅ Consulta por ID (sucesso)
- ✅ Consulta por ID (não encontrado)
- ✅ Validação de dados de entrada
---
## 🔍 Testando a API
### Documentação Interativa
Com a API em execução, acesse a documentação interativa:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
### Ferramentas Alternativas
Você também pode testar utilizando:
- **Postman** para requisições REST
- **cURL** via linha de comando
- **HTTPie** para testes rápidos
---
## 📦 Docker Compose
O arquivo `docker-compose.yml` inclui configuração para:
- **PostgreSQL** - Banco de dados principal
- **Adminer** - Interface web para gerenciamento do banco (opcional)
Para inicializar todo o ambiente:
```bash
docker compose up -d
```
