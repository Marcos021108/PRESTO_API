from fastapi import FastAPI

Presto = FastAPI()

@Presto.get("/")
def home():
    return "Prestoooooooooooooooooooooo"

@Presto.get("/usuarios")
def usuarios():
    return "Aqui será os usuários"

@Presto.get("/avaliacoes")
def avaliacoes():
    return "aqui será as avaliacões"

@Presto.get("/pizzas")
def pizza():
    return "aqui terá as descrições das pizzas"
@Presto.get("/mentores")
def mentores():
    return "obrigado gente"