import  mysql.connector
from fastapi import FastAPI
from fastapi.params import Body

Presto = FastAPI()
usuario = []
avaliacao = []
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
    usuario.append(usuario)
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'INSERT INTO cliente (nome, email, senha) VALUES (%s, %s, %s)'
    valores = (usuario['nome'], usuario['email'], usuario['senha'])
    cursor.execute(comando, valores)
    conexao.commit()
    
    usuario['id'] = cursor.lastrowid
    cursor.close()
    conexao.close()
    return usuario

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
    avaliacao.append(avaliacao)
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'INSERT INTO avaliacao (id_cliente, texto) VALUES (%s, %s)'
    valores = (avaliacao["id_cliente"], avaliacao["texto"])
    cursor.execute(comando, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return avaliacao


@Presto.get("/pizzas")
def pizzass():
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
def pizzas(pizza: dict = Body (...)):
    pizza.append(pizza)
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'INSERT INTO pizza (nome, valor, link_imagem) VALUES (%s, %s, %s)'
    valores = (pizza["nome"], pizza["valor"], pizza["link_img"])
    cursor.execute(comando, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
    
    return pizza

@Presto.get("/mentores")
def mentores():
    return "obrigado gente"

