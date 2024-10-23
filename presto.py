import  mysql.connector
from fastapi import FastAPI
from fastapi.params import Body

Presto = FastAPI()
usuarios = []
avaliacoes = []
pizza = []

@Presto.get("/")
def home():
    return "This is Presto"

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
    cursor.execute(comando)

    usuarios=cursor.fetchall()
    cursor.close()
    conexao.close()
    
    return{"usuarios": usuarios}

@Presto.post("/usuarios")
def usuarios(usuario: dict = Body (...)):
    usuarios.append(usuario)
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'INSERT INTO cliente (nome, email, senha) VALUES ({usuarios['nome']}, {usuarios['email']}, {usuarios['senha']})'
    cursor.execute(comando)

    cursor.close()
    conexao.close()
    return{f"post criado, {usuario['nome']}, {usuario['email']}, {usuario['senha']}"}

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
    cursor.execute(comando)
    

    avaliacoes=cursor.fetchall()
    cursor.close()
    conexao.close()

    return {"avaliacoes":avaliacoes}

@Presto.post("/avaliacoes")
def avaliacoes(avaliacao: dict = Body (...)):
    avaliacoes.append(avaliacao)
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'INSERT INTO avaliacao (id_cliente, texto) VALUES ({avaliacoes['id_cliente']}, {avaliacoes['texto']})'
    cursor.execute(comando)
    cursor.close()
    conexao.close()

    return{f"post criado, {avaliacao['id_cliente']}, {avaliacao['texto']}"}


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
    cursor.execute(comando)

    pizza=cursor.fetchall()
    cursor.close()
    conexao.close()
    
    return{"pizza":pizza}

@Presto.post("/pizza")
def pizza(pizza: dict = Body (...)):
    pizza.append(pizza)
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'INSERT INTO pizza (nome, valor, link_imagem) VALUES ({pizza['nome']}, {pizza['valor']}, {pizza['link_img']})'
    cursor.execute(comando)
    cursor.close()
    conexao.close()
    
    return{f"post criado, {pizza['nome']}, {pizza['valor']}, {pizza['link_img']}"}


@Presto.get("/mentores")
def mentores():
    return "obrigado gente"

