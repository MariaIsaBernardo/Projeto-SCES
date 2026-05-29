
estoque = []
def menu():
    while True:
        print("\n----- Sistema De Controle De Estoque Simplificado (SCES) -----")
        print("1. Adicionar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Atualizar")
        print("5. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
