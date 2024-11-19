import mysql.connector

def conectar_banco_de_dados ():
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database="presto_bd"
    )
    return conexao