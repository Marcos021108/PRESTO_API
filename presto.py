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
    comando2 = f'INSERT INTO cliente (nome, email, senha) VALUES ({usuarios['nome']}, {usuarios['email']}, {usuarios['senha']})'
    cursor.execute(comando2)

    usuarios=cursor.fetchall()
    cursor.close()
    conexao.close()
    
    return{"usuarios": usuarios}

@Presto.post("/usuarios")
def usuarios(usuario: dict = Body (...)):
    usuarios.append(usuario)
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
    comando2 = f'INSERT INTO avaliacao (id_cliente, texto) VALUES ({avaliacoes['id_cliente']}, {avaliacoes['texto']})'
    cursor.execute(comando2)

    avaliacoes=cursor.fetchall()
    cursor.close()
    conexao.close()

    return {"avaliacoes":avaliacoes}

@Presto.post("/avaliacoes")
def avaliacoes(avaliacao: dict = Body (...)):
    avaliacoes.append(avaliacao)
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
    comando2 = f'INSERT INTO pizza (nome, valor, link_imagem) VALUES ({pizza['nome']}, {pizza['valor']}, {pizza['link_img']})'
    cursor.execute(comando2)

    pizza=cursor.fetchall()
    cursor.close()
    conexao.close()
    
    return{"pizza":pizza}

@Presto.post("/pizza")
def pizza(pizza: dict = Body (...)):
    pizza.append(pizza)
    return{f"post criado, {pizza['nome']}, {pizza['valor']}, {pizza['link_img']}"}


@Presto.get("/mentores")
def mentores():
    return "obrigado gente"

