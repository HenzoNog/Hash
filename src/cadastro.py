import re
import hashlib
from Users.py import cadastrarUsuario

def cadastro():

    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    if not re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9]).{8}", senha):
        print("Senha inválida!")
        return
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()   
    #O encode transforma o texto em formato String enviado em bytes para a hashlib 
    #hashlibg.sha256 é o algoritmo matematico do sha256 que processa o bytes que vai ser feito pelo .encode
    #O hexdigest() pega os bytes gerados e retorna uma String para ser armazenada, lida e analisada

    success=cadastrarUsuario(email, senha_hash)

    if success:
        print("Usuário cadastrado com sucesso!")