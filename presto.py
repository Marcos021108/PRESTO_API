import  mysql.connector
from fastapi import FastAPI
from fastapi.params import Body

Presto = FastAPI()
posts = []
postsA = []
postsP = []

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

@Presto.get("/usuL")
def root():
    return{"mensagem": f"{posts}"}

@Presto.get("/usuario{number}")
def root(number:int):
    return{"mensagem": f"{posts[number]}"}

@Presto.post("/postC")
def postC(turtle: dict = Body (...)):
    posts.append(turtle)
    return{f"post criado, {turtle['nome']}, {turtle['email']}, {turtle['senha']}"}

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

@Presto.get("/avaL")
def root():
    return{"mensagem": f"{postsA}"}

@Presto.get("/avaliacoes{number}")
def root(number:int):
    return{"mensagem": f"{postsA[number]}"}

@Presto.post("/postA")
def postA(fox: dict = Body (...)):
    postsA.append(fox)
    return{f"post criado, {fox['id_cliente']}, {fox['texto']}"}


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

@Presto.get("/pizL")
def root():
    return{"mensagem": f"{postsP}"}

@Presto.get("/pizza{number}")
def root(number:int):
    return{"mensagem": f"{postsP[number]}"}

@Presto.post("/postP")
def postP(dragon: dict = Body (...)):
    postsP.append(dragon)
    return{f"post criado, {dragon['nome']}, {dragon['valor']}, {dragon['link_img']}"}


@Presto.get("/mentores")
def mentores():
    return "obrigado gente"

