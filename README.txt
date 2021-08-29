Goal:
Creating a REST API using Python 3.6+ and the FLASK microframework. Using JSON to perform a full CRUD on a CLIENT table. (using SQL Alchemy ORM)

CRUD:
	I. GET (Customer List)
	II. POST (Create Client)
	III. PUT (Edit customer)
	IV. DELETE (Remove client)

Database with fields:
	I. code (primary_key / not null)
	II. name (not null)
	III. corporate name (not null)
	IV. cnpj (not null)
	V. inclusion_date (datetime / not null) (deve ser obtida do formulário, não foi utilizada a data do commit)

API Response Pattern created, with status_code and messages for success or error.

----- // -----

Requirements (1):

Python 3.8.10
Flask 2.0.1
flask_sqlalchemy 2.5.1
psql (PostgreSQL) 12.8
psycopg2 2.9.1

Requirements (2):

Postegresql server running on local system (localhost), port 5432
Database named "smartnx"
User named "user" with password "123456" with rights granted over the referred database.

----- // -----

Postman version 8.11.1 were used to make some tests. Some examples:

(1) Create client(cliente):
In Body>Raw>JSON type:
{
	"nome": "Eduardo Vitor Giancoli Jabour",
	"razaoSocial": "MEI",
	"cnpj": 12345678910,
	"data_inclusao": "2021-08-28T22:10:10"
}
Select "POST" method and send to the address: localhost:5000/cliente

(2) Update for a hipotetical client(cliente) with id(codigo) 123:
In Body>Raw>JSON type:
{
	"nome": "Eduardo Vitor Giancoli Jabour",
	"razaoSocial": "MEI",
	"cnpj": 12345678910,
	"data_inclusao": "2021-08-28T22:10:10"
}
Select "PUT" method and send to the address: localhost:5000/cliente/123

(3) Read data of one hipotetical client(cliente) with id(codigo) 123:
In Body>Raw>JSON type:
{
	"nome": "Eduardo Vitor Giancoli Jabour",
	"razaoSocial": "MEI",
	"cnpj": 12345678910,
	"data_inclusao": "2021-08-28T22:10:10"
}
Select "GET" method and send to the address: localhost:5000/cliente/123

(4) Read data from all clients(clientes):
In Body>Raw>JSON type:
{
	"nome": "Eduardo Vitor Giancoli Jabour",
	"razaoSocial": "MEI",
	"cnpj": 12345678910,
	"data_inclusao": "2021-08-28T22:10:10"
}
Select "GET" method and send to the address: localhost:5000/clientes

(5) Delete client(cliente) with id(codigo) 123 from database
In Body>Raw>JSON type:
{
	"nome": "Eduardo Vitor Giancoli Jabour",
	"razaoSocial": "MEI",
	"cnpj": 12345678910,
	"data_inclusao": "2021-08-28T22:10:10"
}
Select "DELETE" method and send to the address: localhost:5000/cliente/123

----- // -----

OBS: Some of the code comments and variable names are in portuguese. Feel free to contact me in case of any questions



