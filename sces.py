#Ajudinha da bia brito

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
    print("\n--- Listar Produtos ---")
    if opcao == "2":
       print("\n-- Estoque Atual --")
    for produto in pelucia:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Local: {produto[3]}")

def procurarproduto_id():
    print("\n--- Procurar ID ---")
    print("\n-- Procurar Produto --")

    id_busca = int(input("Digite o ID do produto: "))
    procurar = False
        
    for produto in pelucia:
        if produto[0] == id_busca:
            print(f"Produto --> Nome: {produto[1]} | Quantidade: {produto[2]} | Local: {produto[3]}")
            procurar = True
            break

    if procurar == False:
        print("Produto nao encontrado.")

def atualizar_estoque():
    print("\n--- Atualizar Estoque ---")
    print("\n-- Atualizar Estoque --")

    id_busca = int(input("Digite o ID do produto: "))
    achou = False
        
    for produto in pelucia:
        if produto[0] == id_busca:
            achou = True
            print(f"Produto: {produto[1]} (Quantidade Atual: {produto[2]})")
            print("1 - Adicionar | 2 - Retirar ")
            tipo = input("Escolha a operacao: ")
            valor = int(input("Quantidade a alterar: "))
                
            if tipo == "1":
                produto[2] = produto[2] + valor
                print(f"A quantidade de pelucias {produto[1]} foi aumentada!")
            elif tipo == "2":
                produto[2] = produto[2] - valor
                print("A quantidade de pelucias {produto[1]} foi reduzida!")
            break
                    
    if achou == False:
        print("Produto nao encontrado.")
    


def menu():
    while True:
        print("\n--- Menu SCES ---")
        print("\nBem vindo ao menu interativo da SCES! Por favor selecione uma opção:\n")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Procurar")
        print("4 - Atualizar")
        print("5 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            procurarproduto_id()
        elif opcao == "4":
            atualizar_estoque()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


menu()
