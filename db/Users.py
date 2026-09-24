import sqlite3
import os
from src.validaSenha import hashSenha

def criarBanco():
    os.makedirs("db", exist_ok=True)

    conect = sqlite3.connect("db/Users.db")
    cur = conect.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            hash TEXT NOT NULL,
            salt VARBINARY(16) NOT NULL
        )
    """)

    conect.commit()
    conect.close()


def cadastrarUsuario(email, senha_hash, salt):
    conect = sqlite3.connect("db/Users.db")
    cur = conect.cursor()

    try:
        cur.execute(
            "INSERT INTO users (email, hash, salt) VALUES (?, ?, ?)",
            (email, senha_hash, salt)
        )
        conect.commit()
        return True
    except sqlite3.IntegrityError:
        print("Este e-mail já está cadastrado!")
        return False
    finally:
        conect.close()
        
def verificarUsuario(email, senha):
    conect = sqlite3.connect("db/Users.db")
    cur = conect.cursor()
    
    salt = cur.execute("SELECT salt FROM users WHERE email = ?", (email,)).fetchone()
    
    if salt is None:           # Se o email não existir, cria um salt aleatório para não dar pistas sobre a existência do usuário
        salt = os.urandom(16)
        
    senha_hash = hashSenha(senha, salt[0]) if salt else None

    cur.execute(
        "SELECT * FROM users WHERE email = ? AND hash = ?",
        (email, senha_hash)
    )
    user = cur.fetchone()
    conect.close()

    return user is not None