import  mysql.connector
from fastapi import FastAPI

Presto = FastAPI()

@Presto.get("/")
def home():
    return "Prestoooooooooooooooooooooo"

@Presto.get("/usuarios")
def usuarios():
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM cliente'
    cursor.close()
    conexao.close()

@Presto.get("/avaliacoes")
def avaliacoes():
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM avaliacao'
    cursor.close()
    conexao.close()

@Presto.get("/pizzas")
def pizza():
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM pizza'
    cursor.close()
    conexao.close()
    cursor.fetchall
@Presto.get("/mentores")
def mentores():
    return "obrigado gente"

