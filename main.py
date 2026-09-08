import crud
import db_setup

def menu():
    while True:
        print("\n--- Sistema de Estoque de Bicicletas ---")
        print("1. Cadastrar Bicicleta")
        print("2. Ver Estoque")
        print("3. Atualizar Quantidade")
        print("4. Remover Bicicleta")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            modelo = input("Modelo: ")
            marca = input("Marca: ")
            qtd = int(input("Quantidade em estoque: "))
            preco = float(input("Preço de venda (R$): "))
            crud.adicionar_bicicleta(modelo, marca, qtd, preco)
            print("Produto cadastrado com sucesso!")
            
        elif escolha == '2':
            bikes = crud.listar_bicicletas()
            print("\n--- ESTOQUE ATUAL ---")
            for b in bikes:
                print(f"ID {b[0]} | {b[2]} {b[1]} | Estoque: {b[3]} | R$ {b[4]:.2f}")
                
        elif escolha == '3':
            id_bike = int(input("ID do produto: "))
            nova_qtd = int(input("Nova quantidade em estoque: "))
            crud.atualizar_estoque(id_bike, nova_qtd)
            print("Estoque atualizado!")
            
        elif escolha == '4':
            id_bike = int(input("ID do produto a ser removido: "))
            crud.deletar_bicicleta(id_bike)
            print("Produto removido do sistema.")
            
        elif escolha == '5':
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    db_setup.criar_tabelas() # Garante que o banco existe ao rodar
    menu()