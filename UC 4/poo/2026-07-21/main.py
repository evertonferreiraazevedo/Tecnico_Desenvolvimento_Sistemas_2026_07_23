from classeVeiculo import Veiculo

def exibir_menu():
    print(f"\nMENU {Veiculo.nome_estacionamento}")
    print("1. Exibir Informações do Estacionamento")
    print("2. Cadastrar Veículo")
    print("3. Adicionar Horas a um Veículo")
    print("4. Exibir Dados de um Veículo")
    print("5. Calcular Valor")
    print("0. Sair")
    return input("Escolha uma opção: ")

def buscar_veiculo():
    placa = input("Digite a placa do veículo: ").strip()
    for v in Veiculo.patio_estacionamento:
        if v.placa == placa:
            return v
    return None

if __name__ == "__main__":
 
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            Veiculo.exibir_informacoes_estacionamento()

        elif opcao == "2":
            print("\n NOVO CADASTRO")
            placa = input("Digite a placa do veículo: ").strip()
            
            if not Veiculo.validar_placa(placa):
                print("Erro: Placa inválida! Deve conter exatamente 7 caracteres.")
                continue

            ja_cadastrado = False
            for v in Veiculo.patio_estacionamento:
                if v.placa == placa:
                    ja_cadastrado = True
                    break

            if ja_cadastrado:
                print("Erro: Um veículo com esta placa já está cadastrado.")
                continue

            modelo = input("Digite o modelo do veículo: ").strip()
            proprietario = input("Digite o nome do proprietário: ").strip()
            entrada_horas = 0
            novo_veiculo = Veiculo(placa, modelo, proprietario, entrada_horas)
            Veiculo.patio_estacionamento.append(novo_veiculo)
            print(f"Veículo de {proprietario} cadastrado com sucesso!")

        elif opcao == "3":
            print("\n ADICIONAR HORAS ")
            veiculo_encontrado = buscar_veiculo()

            if veiculo_encontrado:
                horas_novas = float(input("Digite a quantidade de horas a adicionar: "))
                veiculo_encontrado.adicionar_horas(horas_novas)
                veiculo_encontrado.__horas_estacionadas = 0
            else:
                print("Veículo não encontrado no pátio.")

        elif opcao == "4":
            print("\nCONSULTAR VEÍCULO ")
            veiculo_encontrado = buscar_veiculo()

            if veiculo_encontrado:
                veiculo_encontrado.exibir_dados()
            else:
                print("Veículo não encontrado no pátio.")

        elif opcao == "5":
            print("\nCALCULAR VALOR ")
            veiculo_encontrado = buscar_veiculo()

            if veiculo_encontrado:
                print(f"O valor do estacionamento é R${veiculo_encontrado.calcular_valor_total():.2f}")
                Veiculo.remover_veiculo_patio(veiculo_encontrado)
            else:
                print("Veículo não encontrado no pátio.")

        elif opcao == "0":
            print("\nEncerrando o sistema do estacionamento. Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")
