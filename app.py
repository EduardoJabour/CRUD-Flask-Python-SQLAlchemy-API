from datetime import datetime
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:123456@localhost:5432/smartnx'
db = SQLAlchemy(app)

class Cliente(db.Model):
    codigo = db.Column(db.Integer, primary_key = True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    razaoSocial = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(20), nullable=False)
    data_inclusao = db.Column(db.DateTime, nullable=False)

    def to_json(self):
        return {"codigo": self.codigo, "nome": self.nome, "razaoSocial": self.razaoSocial, "cnpj": self.cnpj, "data_inclusao": self.data_inclusao}

db.create_all()

# Selecionar Tudo (GET)
@app.route("/clientes", methods=["GET"])
def seleciona_clientes():
    clientes_objetos = Cliente.query.all()
    clientes_json = [cliente.to_json() for cliente in clientes_objetos]
    return gera_resposta(200, "clientes", clientes_json)

# Selecionar Individual (GET)
@app.route("/cliente/<codigo>", methods=["GET"])
def seleciona_cliente(codigo):
    cliente_objeto = Cliente.query.filter_by(codigo=codigo).first()
    cliente_json = cliente_objeto.to_json()

    return gera_resposta(200, "cliente", cliente_json)

# Cadastrar (CREATE)
@app.route("/cliente", methods=["POST"])
def cria_cliente():
    body = request.get_json()
    
    try:
        cliente = Cliente(nome=body["nome"], razaoSocial= body["razaoSocial"], cnpj= body["cnpj"], data_inclusao= body["data_inclusao"])
        db.session.add(cliente)
        db.session.commit()
        return gera_resposta(201, "cliente", cliente.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_resposta(400, "cliente", {}, "Erro ao cadastrar")


# Atualizar (UPDATE)
@app.route("/cliente/<codigo>", methods=["PUT"])
def atualiza_cliente(codigo):
    cliente_objeto = Cliente.query.filter_by(codigo=codigo).first()
    body = request.get_json()

    try:
        if('nome' in body):
            cliente_objeto.nome = body['nome']
        if('razaoSocial' in body):
            cliente_objeto.razaoSocial = body['razaoSocial']
        if('cnpj' in body):
            cliente_objeto.cnpj = body['cnpj']
        if('data_inclusao' in body):
            cliente_objeto.data_inclusao = body['data_inclusao']
        
        db.session.add(cliente_objeto)
        db.session.commit()
        return gera_resposta(200, "cliente", cliente_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_resposta(400, "cliente", {}, "Erro ao atualizar")

# Deletar (DELETE)
@app.route("/cliente/<codigo>", methods=["DELETE"])
def deleta_cliente(codigo):
    cliente_objeto = Cliente.query.filter_by(codigo=codigo).first()

    try:
        db.session.delete(cliente_objeto)
        db.session.commit()
        return gera_resposta(200, "cliente", cliente_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_resposta(400, "cliente", {}, "Erro ao deletar")


def gera_resposta(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run()