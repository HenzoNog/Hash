import re
import db.Users as criarBanco

def main():
    criarBanco.criarBanco()

    while True:
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            from src.cadastro import cadastro
            cadastro()
        elif opcao == "2":
            from src.login import login
            login()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

main()