import  mysql.connector
from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.params import Body
from util import conectar_banco_de_dados


AvaliacaoRouter = APIRouter()


@AvaliacaoRouter.get("/avaliacoes")
def obter_todas_avaliacoes():
    conexao = conectar_banco_de_dados()
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM avaliacao'
    cursor.execute(comando)
    

    avaliacoes=cursor.fetchall()
    cursor.close()
    conexao.close()

    return {"avaliacoes":avaliacoes}

@AvaliacaoRouter.get("/avaliacoes/{id}")
def obter_avaliacao_id(id: int):

    conexao = conectar_banco_de_dados()
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM avaliacao WHERE id = %s'
    valores = (id,)
    cursor.execute(comando, valores)

    avaliacoes = cursor.fetchone()
    cursor.close()
    conexao.close()

    return avaliacoes

@AvaliacaoRouter.put("/avaliacoes/{id}")
def atualizar_avaliacao(id:int, avaliacao: dict = Body (...)):
    
    conexao = conectar_banco_de_dados()
    cursor = conexao.cursor()
    comando = f'UPDATE avaliacao SET texto = %s WHERE Id = %s'
    valores = (avaliacao['texto'], id)
    cursor.execute(comando, valores)
    conexao.commit()

    avaliacao['id'] = id
    cursor.close()
    conexao.close()
    return avaliacao

@AvaliacaoRouter.post("/avaliacoes")
def inserir_avaliacoes(avaliacao: dict = Body (...)):
    conexao = conectar_banco_de_dados()
    cursor = conexao.cursor()
    comando = f'INSERT INTO avaliacao (id_cliente, texto) VALUES (%s, %s)'
    valores = (avaliacao["id_cliente"], avaliacao["texto"])
    cursor.execute(comando, valores)
    conexao.commit()

    avaliacao['id'] = cursor.lastrowid
    cursor.close()
    conexao.close()

    return avaliacao

@AvaliacaoRouter.delete("/deleteUsuario/{id}")
def deletar_avaliacao(id: int):
    conexao = conectar_banco_de_dados()
    cursor = conexao.cursor()
    comando = f'DELETE FROM avaliacao WHERE id = %s'
    valores = (id,)
    cursor.execute(comando, valores)

    cursor.close()
    conexao.close()
    return "avaliacao excluída"