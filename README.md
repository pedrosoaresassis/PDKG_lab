# Template de REST API - CodeIsArt

Sempre que fizer a implementação de uma funcionalidade genérica de REST API, adicionar na lista abaixo.

## IMPORTANTE
Sempre que for implementar uma nova funcionalidade, criar nova branch e criar Pull Request para review.

## Funcionalidades:


### USER --------------------------------------------------------------------------------------------------------------

### URL: http://127.0.0.1:8000/users/CRUD/

### register:
    O usuario se registra com email, username e pass, colocando seus dados dentro do banco de dados

    {
    "username": "shizu",
    "email": "shizu@gmail.com",
    "password": "banana@321_"
    }

### login:
    Com isso iremos direcionalo para parte de login, quando ocorrer o envio do username e password o backend analisa se "banana" Hasheado == DB.pass:"aasdasd2a$sd2asd2$2asd".
    se o login der certo é enviado um token para ele. Fazendo com que ele possa Editar e excluir a conta.

    {
    "username": "shizu",
    "password": "banana@321_"
    }

    token = 116e7b552ab44e443b7723c99c70bb0806e3863f

### update (token):
    Com o token em mão o usuario passa pela verificação da rota UPDATE e DELETE.

    {
        "username": "shizu",
        "email": "test@gmail.com",
        "password": "banana@321_",
        "new_password": "banana@_321"
    }

### delete (token):
    {
        "username": "shizu",
        "password": "banana@321_",
    }


## PRODUCTS -----------------------------------------------------------------------------------------------------------

### URL: http://127.0.0.1:8000/products/products/
Essa rota n precisa de nada pra validar, apenas o token. 
Adicionar futuramente a validação de quem realmente esta auterando o DB

    ____________________________________________
    1. Obter todos os produtos (GET)

    http://127.0.0.1:8000/products/products/
    ____________________________________________

    2. Obter detalhes de um produto (GET por ID)

    http://127.0.0.1:8000/products/products/{id}/
    ____________________________________________

    3. Atualizar um produto (PUT)

    http://127.0.0.1:8000/products/products/{id}/
    ____________________________________________

    4. Excluir um produto (DELETE)

    http://127.0.0.1:8000/products/products/{id}/
    ____________________________________________

### MODEL JSON REQUEST

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





