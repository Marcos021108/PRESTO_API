import  mysql.connector
from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.params import Body
from usuarios import UsuarioRouter
from avaliacao import AvaliacaoRouter
from pizza import PizzaRouter
from hashlib import sha256

Presto = FastAPI()
Presto.include_router(UsuarioRouter)
Presto.include_router(AvaliacaoRouter)
Presto.include_router(PizzaRouter)

@Presto.get("/")
def home():
    return "This is Presto"


