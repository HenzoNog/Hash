import db.Users as criarBanco

def main():
    criarBanco.criarBanco()

    while True:
        print(f"""==========================================
      Hash e senhas em banco de dados

        Menu de opções:
        
        1. Cadastrar usuário
        2. Fazer login
        3. Sair
==========================================
        """)

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
            print("\n\n⚠️  ⚠️  ⚠️   Opção inválida! ⚠️  ⚠️  ⚠️")

main()