pelucia = [
   [3421, "Pato", 458, "Prateleira B-22"],
   [4321, "Jacaré", 305, "Prateleira F-35"],
   [6234, "Gato", 687, "Prateleira A-1"],
   [2340, "Cachorro", 566, "Prateleira A-3"],
   [3456, "Cobra", 354, "Prateleira F-37"]
]

opcao = "0"

def adicionar_produto():
    print("\n--- Adicionar Produto ---")
    print("\n-- Novo Produto --")
    id_produto = int(input("Digite o ID (Número): "))
    nome = input("Digite o Nome: ")
    qtd = int(input("Digite a Quantidade: "))
    local = input("Digite a Localização (Ex: A-01): ")

    pelucia.append([id_produto, nome, qtd, local])
    print("Produto cadastrado!")


def listar_produtos():
    print("\n--- Função Listar Produtos ---")
    if opcao == "2":
       print("\n-- Estoque Atual --")
    for produto in pelucia:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Local: {produto[3]}")

def buscarproduto_id():
    print("\n--- Função Buscar por ID ---")

def atualizar_estoque():
    print("\n--- Função Atualizar Estoque ---")


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
