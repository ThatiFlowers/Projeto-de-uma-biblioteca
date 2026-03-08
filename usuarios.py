import sqlite3
conexao = sqlite3.connect("pspec/projetinho_biblio.db")
cursor = conexao.cursor()

def listar_usuarios() :
    cursor.execute (" SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    return usuarios

cursor.execute("""
        CREATE TABLE if NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT
          )
               """
               )

usuarios_lista = [
    ("Matheus Lima", "2199000-0000"),
    ("Marta Rocha", "2199100-0001"),
    ("Joana Brito","2199200-0002"),
    ("Beth Maria F.","3399000-0003"),
    ("Beatriz cardoso","3299000-0004")
]

cursor.executemany ('''
INSERT INTO usuarios (nome, telefone)
VALUES(?,?)
               ''', usuarios_lista)

conexao.commit()

#cursor.close()
#conexao.close()
