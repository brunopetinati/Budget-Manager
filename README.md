# Budget Manager

**Versão 1.0.0**

## Instalação

no terminal, na raíz do projeto, digitar o seguinte comando:
docker-compose up
Em seguida usar aplicativos para requisição como Postman ou Insomnia para utilizar as rotas.

Caso não se deseja utilizar o Docker para rodar o aplicativo, também há a opção de criar um arquivo .env seguindo as variáveis do arquivo "env_example". O arquivo "detalhes_postgresql.md" contém informações de como configurar um banco PostgreSQL localmente.

## Sobre:

O app Budget Manager é composto de 4 rotas principais. São elas: User, MyWallet, Login e Transactions.
A rota User, quando no método POST, é usada para registrar um novo usuário no app.
A rota Login é usada para obter Token, que contém informações do usuário para sua devida identificação ao realizar transações. Para fazer o Login é necessário que o usuário insira seu email e senha. 
A rota MyWallet, quando no método GET, é usada para verificar informações pessoais da conta, como o saldo disponível, por exemplo.
A rota Transactions no método GET, lista todas as transações realizadas para conta identificada pelo token. Ou seja, o usuário logado poderá verificar todas as suas transações, mas não conseguirá ver as transações de outros usuários.
A rota Transactions, quando no método POST, cria uma nova transação.


A não ser que esteja sendo usado um outro prefixo, todas as rotas devem ser utilizadas como prefixo http://127.0.0.1:8000/

Exemplo, a rota User, será http://127.0.0.1:8000/api/accounts


## Rotas e requisições


### User

/api/accounts/

método: POST

Cria conta de usuário.

Exemplo de requisição:

{
  "username": "brunopetinati6",
  "first_name":"Bruno", 
  "last_name":"Petinati", 
  "full_name":"Bruno Petinati",
  "email":"brunopetinati6@ig.com.br",
  "date_of_birth":"1989-09-16",
  "CPF":"55555555555",
  "wallet": 50,
  "password":"1234"
}

### Login

/api/login/

método: POST

Loga na conta. Obtém token de identificação.

Exemplo de requisição:

{
   "email":"brunopetinati6@ig.com.br",
   "password":"1234"
}

### MyWallet

/api/mywallet/

método GET
necessário Token

Vê seu saldo.

### Transactions - POST

/api/transactions/

método: POST
necessário Token

Cria nova transação para determinada conta.
"transaction_type" pode receber os valores "credit" ou "debt".
No caso de "credit", o valor será creditado na conta da pessoa que está logada.
No caso de "debt", o valor será debitado da conta da pessoa que está logada. O valor de débito não pode ser maior do que o saldo disponível na conta.

Exemplo de requisição:

{
   "description":"Ração para gatos",
   "transaction_type":"credit",
   "amount": "175.00"
}

### Transactions - GET

/api/transactions/

método: GET
necessário Token

Lista todas as transações já efetuadas.


## Testes

Para executar os testes, é necessário digitar no terminal, na raíz do projeto o seguinte comando:

TEST=TEST python manage.py test -v 2

Caso queira um relatório de testes, rodar o seguinte comando:

TEST=TEST python manage.py test -v 2 &> report.txt





