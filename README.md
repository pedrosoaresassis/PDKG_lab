# Template de REST API - CodeIsArt

Sempre que fizer a implementação de uma funcionalidade genérica de REST API, adicionar na lista abaixo.

## IMPORTANTE
Sempre que for implementar uma nova funcionalidade, criar nova branch e criar Pull Request para review.

## Funcionalidades:


### -> REGISTER -> LOGIN -> UPDATE -> DELETE

### Register:
    O usuario se registra com email, username e pass, colocando seus dados dentro do banco de dados

    {
    "username": "shizu",
    "email": "shizu@gmail.com",
    "password": "banana@321_"
    }

### Login:
    Com isso iremos direcionalo para parte de login, quando ocorrer o envio do username e password o backend analisa se "banana" Hasheado == DB.pass:"aasdasd2a$sd2asd2$2asd".
    se o login der certo é enviado um token para ele. Fazendo com que ele possa Editar e excluir a conta.

    {
    "username": "shizu",
    "password": "banana@321_"
    }

    token = 116e7b552ab44e443b7723c99c70bb0806e3863f

### UPDATE (token):
    Com o token em mão o usuario passa pela verificação da rota UPDATE e DELETE.

    {
        "username": "shizu",
        "email": "test@gmail.com",
        "password": "banana@321_",
        "new_password": "banana@_321"
    }

### DELETE (token):
    {
        "username": "shizu",
        "password": "banana@321_",
    }



