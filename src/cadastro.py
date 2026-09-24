import os
from email_validator import validate_email, EmailNotValidError
from db.Users import cadastrarUsuario
from src.validaSenha import validarSenha, hashSenha

def cadastro():
    while True:
        email = input("Digite seu e-mail: ")
        try:
            email = validate_email(email).email
            break
        except EmailNotValidError as e:
            print(f"\n\n⚠️  ⚠️  ⚠️   E-mail inválido! Por favor, insira um e-mail válido.\n: {str(e)}")

    while True:
        senha = input("Digite sua senha: ")
        if not validarSenha(senha):
            print("\n⚠️  ⚠️  ⚠️   Senha inválida! A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula, um número, um caractere especial e ter exatamente 8 caracteres.")
        else:
            break
        
    salt = os.urandom(16)
        
    senha_hash = hashSenha(senha, salt)

    success=cadastrarUsuario(email, senha_hash, salt)

    if success:
        print("Usuário cadastrado com sucesso!")