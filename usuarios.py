import  mysql.connector
from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.params import Body
from hashlib import sha256
from util import conectar_banco_de_dados


UsuarioRouter = APIRouter()


@UsuarioRouter.get("/usuarios")
def obter_todos_usuarios():
    conexao = conectar_banco_de_dados()
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM cliente'
    cursor.execute(comando)

    usuarios=cursor.fetchall()
    cursor.close()
    conexao.close()
    
    return{"usuarios": usuarios}

@UsuarioRouter.post("/usuarios")
def inserir_usuarios(usuario: dict = Body (...)):
    conexao = conectar_banco_de_dados()
    cursor = conexao.cursor()
    comando = f'INSERT INTO cliente (nome, email, senha) VALUES (%s, %s, %s)'
    valores = (usuario['nome'], usuario['email'], senhaCod)
    senhaCod = sha256(usuario['senha'].encode()).digest
    cursor.execute(comando, valores)
    conexao.commit()
    
    usuario['id'] = cursor.lastrowid
    cursor.close()
    conexao.close()
    return usuario

@UsuarioRouter.get("/usuarios/{id}")
def obter_usuario_id(id: int):
    conexao = conectar_banco_de_dados()
    cursor = conexao.cursor(dictionary=True)
    comando = f'SELECT * FROM cliente WHERE id = %s'
    valores = (id,)
    cursor.execute(comando, valores)

    usuario = cursor.fetchone()
    cursor.close()
    conexao.close()

    return usuario


@UsuarioRouter.put("/usuarios/{id}")
def atualizar_usuarios(id:int, usuario: dict = Body (...)):
    conexao = conectar_banco_de_dados()
    cursor = conexao.cursor()
    comando = f'UPDATE cliente SET nome = %s, senha = %s WHERE Id = %s'
    valores = (usuario['nome'], senhaCod, id)
    senhaCod = sha256(usuario['senha'].encode()).digest
    cursor.execute(comando, valores)
    conexao.commit()

    usuario['id'] = id
    cursor.close()
    conexao.close()
    return usuario