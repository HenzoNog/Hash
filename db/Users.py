import sqlite3
import os


def criarBanco():
    os.makedirs("db", exist_ok=True)  # garante que a pasta "db" existe

    conect = sqlite3.connect("db/Users.db")
    cur = conect.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            hash TEXT NOT NULL
        )
    """)

    conect.commit()
    conect.close()


def cadastrarUsuario(email, senha_hash):
    conect = sqlite3.connect("db/Users.db")
    cur = conect.cursor()

    try:
        cur.execute(
            "INSERT INTO users (email, hash) VALUES (?, ?)",
            (email, senha_hash)
        )
        conect.commit()
        return True
    except sqlite3.IntegrityError:
        print("Este e-mail já está cadastrado!")
        return False
    finally:
        conect.close()