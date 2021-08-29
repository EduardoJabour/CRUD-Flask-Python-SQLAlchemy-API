Using Python 3.6+ and the FLASK microframework.
Creating a REST API using JSON to perform a full CRUD on a CLIENT table. (using SQL Alchemy ORM)
	I. GET (Customer List)
	II. POST (Create Client)
	III. PUT (Edit customer)
	IV. DELETE (Remove client)

d. Create Migrations to create the table in the database with the fields:
i. code (primary_key / not null) ,
ii. name (not null)
iii. corporate name (not null)
iv. cnpj (not null),
v. inclusion_date (datetime / not null) (deve ser obtida do formulário, não foi utilizada a data do commit)
and. Create an API Response Pattern, with status_code and messages.
success or error, for example.

{
"status": 200,
"message": "Client created successfully"
"error": "null"
}

Opted for not using an environment

Requirements:

Python 3.8.10
Flask 2.0.1
flask_sqlalchemy 2.5.1
psql (PostgreSQL) 12.8
psycopg2 2.9.1

A aplicação requer:

Servidor postgresql rodando no sistema local (localhost), na porta 5432
Banco de dados smartnx
Usuário user (senha 123456) com direitos concedidos sobre o banco acima

OBS: Some of the code comments and variable names are in portuguese. Feel free to contact me in case of any questions

Tests with Postman were made.