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
def obter_usuario_id(id: int):

    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM cliente WHERE id = %s'
    valores = (id,)
    cursor.execute(comando, valores)

    usuario = cursor.fetchone()
    cursor.close()
    conexao.close()

    return usuario


@Presto.put("/usuarios/{id}")
def atualizar_usuarios(id:int, usuario: dict = Body (...)):

    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'UPDATE cliente SET nome = %s, senha = %s WHERE Id = %s'
    valores = (usuario['nome'], usuario['senha'], id)
    cursor.execute(comando, valores)
    conexao.commit()

    usuario['id'] = id
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
def obter_avaliacao_id(id: int):

    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM avaliacao WHERE id = %s'
    valores = (id,)
    cursor.execute(comando, valores)

    avaliacoes = cursor.fetchone()
    cursor.close()
    conexao.close()

    return avaliacoes

@Presto.put("/avaliacoes/{id}")
def atualizar_avaliacao(id:int, avaliacao: dict = Body (...)):
    
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'UPDATE avaliacao SET texto = %s WHERE Id = %s'
    valores = (avaliacao['texto'], id)
    cursor.execute(comando, valores)
    conexao.commit()

    avaliacao['id'] = id
    cursor.close()
    conexao.close()
    return avaliacao

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
def obter_pizzas_id(id: int):

    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM pizza WHERE id = %s'
    valores = (id,)
    cursor.execute(comando, valores)

    pizza = cursor.fetchone()
    cursor.close()
    conexao.close()

    return pizza

@Presto.put("/pizzas/{id}")
def atualizar_pizzas(id:int, pizza: dict = Body (...)):
    
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'UPDATE pizza SET nome = %s, valor = %s, link_imagem WHERE Id = %s'
    valores = (pizza['nome'], pizza['valor'], pizza['link_imagem'], id)
    cursor.execute(comando, valores)
    conexao.commit()

    pizza['id'] = id
    cursor.close()
    conexao.close()
    return pizza

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

