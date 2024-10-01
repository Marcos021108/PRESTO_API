import  mysql.connector
from fastapi import FastAPI

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
)
cursor = conexao.cursor(dictionary=True)

Presto = FastAPI()

@Presto.get("/")
def home():
    return "Prestoooooooooooooooooooooo"

@Presto.get("/usuarios")
def usuarios():
    comando = f'SELECT * FROM cliente'
    cursor.close()
    conexao.close()

@Presto.get("/avaliacoes")
def avaliacoes():
    comando = f'SELECT * FROM avaliacao'
    cursor.close()
    conexao.close()

@Presto.get("/pizzas")
def pizza():
    comando = f'SELECT * FROM pizza'
    cursor.close()
    conexao.close()

@Presto.get("/mentores")
def mentores():
    return "obrigado gente"

