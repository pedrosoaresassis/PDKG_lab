# Template de API REST - Code&Art

Um modelo completo para construção de APIs REST robustas usando Django e Django REST Framework. Este template fornece uma base sólida com funcionalidades pré-construídas para requisitos comuns de API.

## Sobre Este Projeto

Este template serve como ponto de partida para o desenvolvimento de APIs REST com Django. Inclui autenticação de usuário pré-configurada, gerenciamento de produtos e segue as melhores práticas para implementação do Django REST Framework.

## Tecnologias Utilizadas

- Django 5.1.7
- Django REST Framework 3.16.0
- Autenticação por Token
- SQLite (padrão, pode ser configurado para outros bancos de dados)
- Princípios de design RESTful API
- djangorestframework-simplejwt 5.2.1

## Começando

### Pré-requisitos
- Python 3.8+
- pip

### Instalação

1. Clone o repositório
```bash
git clone https://github.com/CodeIsArtStudio/djangoapitemplate.git
cd djangoapitemplate
```

2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute as migrações
```bash
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento
```bash
python manage.py runserver
```

A API estará disponível em http://127.0.0.1:8000/

## Estrutura do Projeto

```
djangoapitemplate/
├── users/                  # App de autenticação de usuários
├── products/               # App de gerenciamento de produtos
├── core/                   # Funcionalidades principais
├── manage.py               # Script de gerenciamento do Django
└── requirements.txt        # Dependências do projeto
```

## Funcionalidades:

Sempre que fizer a implementação de uma funcionalidade genérica de REST API, adicionar na lista abaixo.

### USER --------------------------------------------------------------------------------------------------------------

#### URL: http://127.0.0.1:8000/users/CRUD/

#### Register:
O usuário se registra com email, username e password, colocando seus dados dentro do banco de dados

```json
{
    "username": "shizu",
    "email": "shizu@gmail.com",
    "password": "banana@321_"
}
```

#### Login:
Com isso iremos direcioná-lo para parte de login, quando ocorrer o envio do username e password o backend analisa se "banana" Hasheado == DB.pass:"aasdasd2a$sd2asd2$2asd".
Se o login der certo é enviado um token para ele. Fazendo com que ele possa editar e excluir a conta.

```json
{
    "username": "shizu",
    "password": "banana@321_"
}
```

Resposta:
```
token = 116e7b552ab44e443b7723c99c70bb0806e3863f
```

#### Update (token necessário):
Com o token em mãos o usuário passa pela verificação da rota UPDATE e DELETE.

```json
{
    "username": "shizu",
    "email": "test@gmail.com",
    "password": "banana@321_",
    "new_password": "banana@_321"
}
```

#### Delete (token necessário):
```json
{
    "username": "shizu",
    "password": "banana@321_"
}
```

### PRODUCTS -----------------------------------------------------------------------------------------------------------

#### URL: http://127.0.0.1:8000/products/products/
Essa rota não precisa de nada para validar, apenas o token. 
Adicionar futuramente a validação de quem realmente está alterando o DB

##### 1. Obter todos os produtos (GET)
```
http://127.0.0.1:8000/products/products/
```

##### 2. Obter detalhes de um produto (GET por ID)
```
http://127.0.0.1:8000/products/products/{id}/
```

##### 3. Atualizar um produto (PUT)
```
http://127.0.0.1:8000/products/products/{id}/
```

##### 4. Excluir um produto (DELETE)
```
http://127.0.0.1:8000/products/products/{id}/
```

#### MODELO DE REQUISIÇÃO JSON

```json
{
    "name": "Produto 1",
    "description": "Descrição do Produto 1",
    "category": "Tecnologia",
    "price": 1500.00,
    "stock_quantity": 10,
    "image_url": "https://exemplo.com/imagens/produto1.jpg",
    "tags": ["promoção"],
    "brand": "Marca X"
}
```

## Autenticação da API

Esta API usa autenticação baseada em token. Para acessar endpoints protegidos:

1. Obtenha um token através do endpoint de login
2. Inclua o token no cabeçalho Authorization das suas requisições:
   ```
   Authorization: Token 116e7b552ab44e443b7723c99c70bb0806e3863f
   ```

## Tratamento de Erros

A API retorna códigos de status HTTP padrão:

- 200: Sucesso
- 201: Criado
- 400: Requisição Inválida
- 401: Não Autorizado
- 403: Proibido

As respostas de erro incluem uma mensagem explicando o erro.

## Contribuindo

1. Crie uma nova branch para sua funcionalidade
2. Implemente suas alterações
3. Crie um Pull Request para revisão
4. Certifique-se de que todos os testes passam antes de enviar