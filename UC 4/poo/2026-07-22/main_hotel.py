# main.py
from classes_hotel import Quarto, Hotel

def exibir_menu():
    print("\nSISTEMA DE HOTEL")
    print("1. Cadastrar Novo Quarto")
    print("2. Verificar Disponibilidade por Tipo")
    print("3. Reservar um Quarto")
    print("4. Liberar um Quarto")
    print("5. Listar Todos os Quartos")
    print("0. Sair")

hotel = Hotel()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Cadastrar Novo Quarto ---")
        numero = int(input("Número do quarto: "))
        
        ja_existe = False
        for q in Hotel.quartos_cadastrados:
            if q.numero == numero:
                ja_existe = True
                break
                
        if ja_existe:
            print("Erro: Já existe um quarto com este número!")
            continue
            
        tipo = input("Tipo (simples, duplo, suite): ")
        novo_quarto = Quarto(numero, tipo)
        Hotel.adicionar_quarto(novo_quarto)

    elif opcao == "2":
        print("\n--- Verificar Disponibilidade ---")
        tipo = input("Digite o tipo de quarto (simples, duplo, suite): ")
        
        disponivel = Hotel.verificar_disponibilidade(tipo)
        if disponivel:
            print(f"Sim! Temos quartos do tipo '{tipo}' disponíveis.")
        else:
            print(f"Não. Não há quartos do tipo '{tipo}' disponíveis no momento.")

    elif opcao == "3":
        print("\n--- Reservar um Quarto ---")
        num_reserva = int(input("Digite o número do quarto que deseja reservar: "))
        
        quarto_encontrado = None
        for q in Hotel.quartos_cadastrados:
            if q.numero == num_reserva:
                quarto_encontrado = q
                break
        
        if quarto_encontrado:
            hotel.reservar_quarto(quarto_encontrado)
        else:
            print("Quarto não encontrado no sistema.")

    elif opcao == "4":
        print("\n--- Liberar um Quarto ---")
        num_liberar = int(input("Digite o número do quarto que deseja liberar: "))
        quarto_encontrado = None
        for q in Hotel.quartos_cadastrados:
            if q.numero == num_liberar:
                quarto_encontrado = q
                break
        if quarto_encontrado:
            hotel.liberar_quarto(quarto_encontrado)
        else:
            print("Erro: Quarto não encontrado no sistema.")

    elif opcao == "5":
        print("\n--- Lista de Quartos Cadastrados ---")
        if not Hotel.quartos_cadastrados:
            print("Nenhum quarto cadastrado até o momento.")
        else:
            for q in Hotel.quartos_cadastrados:
                print(f"Quarto N° {q.numero} | Tipo: {q.tipo} | Status: {q.disponivel}")

    elif opcao == "0":
        print("\nSaindo do sistema... Até logo!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
