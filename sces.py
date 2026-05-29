
estoque = []

def adicionar_produto():
    print("\n--- Função Adicionar Produto ---")

def listar_produtos():
    print("\n--- Função Listar Produtos  ---")

def buscar_produto_por_id():
    print("\n--- Função Buscar por ID ---")

def atualizar_estoque():
    print("\n--- Função Atualizar Estoque ---")

def menu():
    while True:
        print("\n--- MENU SCES ---")
        print("1. Adicionar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Atualizar")
        print("5. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto_por_id()
        elif opcao == "4":
            atualizar_estoque()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


menu()