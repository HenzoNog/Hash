from db.Users import verificarUsuario

def login():
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    if verificarUsuario(email, senha):
        print("Login bem-sucedido!")
    else:
        print("E-mail ou senha incorretos!")
