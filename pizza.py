import  mysql.connector
from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.params import Body



PizzaRouter = APIRouter()


@PizzaRouter.get("/pizzas")
def obter_todas_pizzas():
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

@PizzaRouter.get("/pizzas/{id}")
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

@PizzaRouter.put("/pizzas/{id}")
def atualizar_pizzas(id:int, pizza: dict = Body (...)):
    
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    cursor = conexao.cursor()
    comando = f'UPDATE pizza SET nome = %s, valor = %s, link_imagem = %s WHERE Id = %s'
    valores = (pizza['nome'], pizza['valor'], pizza['link_img'], id)
    cursor.execute(comando, valores)
    conexao.commit()

    pizza['id'] = id
    cursor.close()
    conexao.close()
    return pizza

@PizzaRouter.post("/pizzas")
def inserir_pizzas(pizza: dict = Body (...)):
    
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