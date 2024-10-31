import  mysql.connector
from fastapi import FastAPI
from fastapi.params import Body

Presto = FastAPI()

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

@Presto.get("/usuarios/{id}")
async def read_item(id: int):
    id_passado = id
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM cliente WHERE id = (id_passado)'


@Presto.put("/usuarios/{id}")
def usuarios(usuario: dict = Body (...)):
    id_passado = id
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'UPDATE cliente SET texto = textoPassado WHERE Id = (idPassado)'
    valores = (usuario['texto'])
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

@Presto.get("/avaliacoes/{id}")
async def read_itens(id: int):
    id_passado = id
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM avaliacao WHERE id = (id_passado)'
    return {"item_id": id}

@Presto.post("/avaliacoes")
def avaliacoes(avaliacao: dict = Body (...)):
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

    avaliacao['id'] = cursor.lastrowid
    cursor.close()
    conexao.close()

    return avaliacao


@Presto.get("/pizzas")
def pizzas():
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

@Presto.get("/pizzas/{id}")
async def read_itens(id: int):
    id_passado = id
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM pizza WHERE id = (id_passado)'
    return {"item_id": id}

@Presto.post("/pizzas")
def pizzas(pizza: dict = Body (...)):
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

    pizza['id'] = cursor.lastrowid
    cursor.close()
    conexao.close()
    
    return pizza

@Presto.get("/mentores")
def mentores():
    return "obrigado gente"

