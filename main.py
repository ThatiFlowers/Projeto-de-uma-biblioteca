# importando o FastAPI
from fastapi import FastAPI

app = FastAPI ( )

livros = [
        {"titulo": "Cem anos de solidão", "autor": "Gabriel García Márquez"},
        {"titulo": "Crepúsculo", "autor": "Stephenie Meyer"},
        {"titulo": "Amanhecer", "autor":"Stephenie Meyer"},
        {"titulo": "Eclipse", "autor": "Stephenie Meyer"},
        {"titulo": "O Alquimista","autor": "Paulo Coelho"},
        {"titulo": "O colecionador", "autor":"John Fowels"},
        {"titulo": "Você fica tão sozinho às vezes que até faz uvsentido","autor":
         "Bukowski"}
         ]

# buscar dados
@app.get("/")
def inicio ():
    return {"mensagem": "API da Biblioteca funcionando"} 
 
@app.get("/livros")
def listar_livros():
    return livros

@app.post("/livros")
def adicionar_livro (livro: dict):
    livros.append (livro)
    return {"mensagem": "livro adicionado", "livro": livro}

@app.delete("/livros/{indice}")
def deletar_livro(indice:int):
    livro = livros.pop(indice)
    return {"mensagem": "livro removido", "livro": livro}

from spec.usuarios import listar_usuarios
@app.get("/usuarios")
def get_usuarios():
    lista = listar_usuarios()
    return {"usuarios":list}


