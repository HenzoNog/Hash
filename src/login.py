from db.Users import verificarUsuario

def login():
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    if verificarUsuario(email, senha):
        print("\nLogin bem-sucedido!")
    else:
        print("\nE-mail ou senha incorretos!")
