# Flix API

## 📘 Sobre

API RESTful para gerenciamento de informações sobre filmes desenvolvida usando Django e Django REST framework.

Essa API é consumida por uma aplicação em [Streamlit](https://github.com/elainefs/flix-app-streamlit) para visualização dos dados.

## 💻️ Tecnologias

- Python
- Django
- Django REST framework
- SQLite

## ✅ Funcionalidade

- [x] Autenticação com JWT para proteger os endpoints
- [x] Listagem, criação, atualização e deleção de atores/atrizes
- [x] Listagem, criação, atualização e deleção de gêneros de filmes
- [x] Listagem, criação, atualização e deleção de filmes
- [x] Listagem, criação, atualização e deleção de avaliações de filmes
- [x] Listagem das estatísticas dos filmes cadastrados e avaliados
- [x] Django Command para adicionar atores/atrizes a partir de arquivo .csv

## ⚙️ Como usar

Para executar essa aplicação siga os seguintes passos:

1. Clone o repositório

```bash
git clone https://github.com/elainefs/django-flix-api.git

cd django-flix-api
```

2. Crie e ative um ambiente virtual

```bash
python3 -m venv .venv # Para Windows use: python -m venv .venv
source .venv/bin/activate  # Para Windows use: .venv\Scripts\activate
```

3. Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

4. Execute as migrações no banco de dados

```bash
python3 manage.py migrate
```

5. Crie um super usuário

```bash
python3 manage.py createsuperuser
```

6. Popule o banco com atores e atrizes

```bash
python3 manage.py import_actors actors.csv
```

7. Execute a aplicação

```bash
python3 manage.py runserver
```

A aplicação estará disponível em `http://localhost:8000`.

O gerenciamento pode ser feito através da interface do Django Admin em: `http://localhost:8000/admin/`

Você pode interagir com a API utilizando ferramentas como Postman, Insomnia, entre outras.

## 🔗 Endpoints da API

### Autenticação JWT

Para ter acesso aos dados da API é necessário um token JWT.

O access token possui validade de 1 dia e o refresh de 7 dias.

#### Criação de Token

POST - `http://localhost:8000/api/v1/authentication/token/`

Passe as informações do usuário cadastrado no sistema no body da requisição:

```
{
    "username": "admin",
    "password": "admin"
}
```

#### Verificação do Token

POST - `http://localhost:8000/api/v1/authentication/token/verify/`

Passe o access token obtido na criação no body da requisição:

```
{
    "token": "access_token"
}
```

#### Refresh Token

POST - `http://localhost:8000/api/v1/authentication/token/refresh/`

Passe o refresh token obtido na criação no body da requisição:

```
{
    "refresh": "refresh_token"
}
```

### Gêneros de Filmes

#### Criar gênero de filme

POST - `http://localhost:8000/api/v1/genres/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Request Body:

```json
{
  "name": "Ficção"
}
```

#### Listar todos os gêneros

GET - `http://localhost:8000/api/v1/genres/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

#### Listar gênero por ID

GET - `http://localhost:8000/api/v1/genres/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor       |
| ----- | ----------- |
| id    | id_do_filme |

#### Atualizar gênero

PUT - `http://localhost:8000/api/v1/genres/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor       |
| ----- | ----------- |
| id    | id_do_filme |

Request Body:

```json
{
  "name": "Ficção Científica"
}
```

#### Excluir gênero

DELETE - `http://localhost:8000/api/v1/genres/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor       |
| ----- | ----------- |
| id    | id_do_filme |

### Atore/Atrizes

#### Criar Ator/Atriz

POST - `http://localhost:8000/api/v1/actors/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Request Body:

```json
{
  "name": "Fernanda Torres",
  "birthday": "1965-09-15",
  "nationality": "BRAZIL"
}
```

Atualmente só é possível cadastrar nacionalidades "BRAZIL" e "USA".

#### Listar todos os atores/atrizes

GET - `http://localhost:8000/api/v1/actors/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

#### Listar ator/atriz por ID

GET - `http://localhost:8000/api/v1/actors/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor      |
| ----- | ---------- |
| id    | id_do_ator |

#### Atualizar ator/atriz

PUT - `http://localhost:8000/api/v1/actors/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor      |
| ----- | ---------- |
| id    | id_do_ator |

Request Body:

```json
{
  "name": "Fernanda Torres",
  "birthday": "1965-09-15",
  "nationality": "BRAZIL"
}
```

#### Excluir ator/atriz

DELETE - `http://localhost:8000/api/v1/actors/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor      |
| ----- | ---------- |
| id    | id_do_ator |

### Filmes

#### Criar filme

POST - `http://localhost:8000/api/v1/movies/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Request Body:

```json
{
  "title": "As branquelas",
  "release_date": "2004-06-23",
  "resume": "Dois agentes do FBI desonrados se disfarçam em um esforço para proteger duas herdeiras de um plano de sequestro.",
  "genre": 2,
  "actors": [1]
}
```

#### Listar todos os filmes

GET - `http://localhost:8000/api/v1/movies/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

#### Listar filmes por ID

GET - `http://localhost:8000/api/v1/movies/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor       |
| ----- | ----------- |
| id    | id_do_filme |

#### Atualizar filme

PUT - `http://localhost:8000/api/v1/movies/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor       |
| ----- | ----------- |
| id    | id_do_filme |

Request Body:

```json
{
  "title": "As branquelas",
  "release_date": "2004-06-23",
  "resume": "Dois agentes do FBI desonrados se disfarçam em um esforço para proteger duas herdeiras de um plano de sequestro.",
  "genre": 2,
  "actors": [1]
}
```

#### Excluir filme

DELETE - `http://localhost:8000/api/v1/movies/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor       |
| ----- | ----------- |
| id    | id_do_filme |

#### Estatísticas dos filmes

GET - `http://localhost:8000/api/v1/movies/stats/`

### Avaliação

#### Criar avaliação

POST - `http://localhost:8000/api/v1/reviews/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Request Body:

```json
{
  "stars": 5,
  "movie": 3
}
```

#### Listar todas as avaliações

GET - `http://localhost:8000/api/v1/reviews/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

#### Listar avaliações por ID

GET - `http://localhost:8000/api/v1/reviews/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor        |
| ----- | ------------ |
| id    | id_da_review |

#### Atualizar avaliação

PUT - `http://localhost:8000/api/v1/reviews/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor        |
| ----- | ------------ |
| id    | id_da_review |

Request Body:

```json
{
  "stars": 5,
  "movie": 3
}
```

#### Excluir avaliação

DELETE - `http://localhost:8000/api/v1/reviews/{id}/`

Campos do header da requisição:

| Campo         | Valor        |
| ------------- | ------------ |
| Authorization | Bearer token |

Parâmetros

| Campo | Valor        |
| ----- | ------------ |
| id    | id_da_review |

## 📄 Licença

Este projeto está sobre a licença MIT. Veja o arquivo [LICENSE](https://github.com/elainefs/django-flix-api/blob/main/LICENSE) para mais informações.

---

Made with ❤️ by [Elaine Ferreira](https://github.com/elainefs)
