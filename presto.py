import  mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
)
cursor = conexao.cursor()
from fastapi import FastAPI

Presto = FastAPI()

@Presto.get("/")
def home():
    return "Prestoooooooooooooooooooooo"

@Presto.get("/usuarios")
def usuarios():
    comando = f'SELECT * FROM cliente'

@Presto.get("/avaliacoes")
def avaliacoes():
    comando = f'SELECT * FROM avaliacao'

@Presto.get("/pizzas")
def pizza():
    comando = f'SELECT * FROM pizza'
@Presto.get("/mentores")
def mentores():
    return "obrigado gente"

cursor.close()
conexao.close()