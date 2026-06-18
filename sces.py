estoque = []

def menu():
    while True:
        print("\n--- Menu SCES ---")
        print("\nBem vindo ao menu interativo da SCES! Por favor selecione uma opção:\n")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Atualizar")
        print("5 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscarproduto_id()
        elif opcao == "4":
            atualizar_estoque()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


menu()