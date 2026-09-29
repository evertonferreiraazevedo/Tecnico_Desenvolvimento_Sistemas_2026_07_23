from classesalao import Cliente, Servico, Agendamento #, SalaoBeleza

#Caso queira deixar o armazenamento dos objetos dentro do arquivo main, basta comentar as linhas que possuem o prefixo 'meu_salao.' antes das listas e habilitar a linha correspondente que está logo acima.
clientes = []
servicos = []
agendamentos = []


def cadastrar_cliente():
    print("\n=== Cadastro de Cliente ===")
    nome = input("Nome: ")
    
    cliente_existente = False
    for nome_cliente in clientes: 
    #for nome_cliente in meu_salao.clientes:
        if nome_cliente.nome == nome:
            cliente_existente = True
            break
    
    if cliente_existente:
        print(f"O Cliente {nome} ja esta cadastrado")
    else:
        cpf = input("CPF: ")
        for nome_cliente in clientes: 
        #for nome_cliente in meu_salao.clientes:
            if nome_cliente.cpf == cpf:
                print("CPF já Cadastrado!")
                return
        
        telefone = input("Telefone: ")
        email = input("E-mail: ")

        cliente = Cliente(nome, cpf, telefone, email)
        clientes.append(cliente)
        #meu_salao.clientes.append(cliente)

        print("Cliente cadastrado com sucesso!\n")

def cadastrar_servico():
    print("\n=== Cadastro de Serviço ===")

    nome = input("Nome do serviço: ")
    
    servico_existente = False
    for nome_servico in servicos:
    #for nome_servico in meu_salao.servicos:
        if nome_servico.nome == nome:
            servico_existente = True
            break
    
        
    if servico_existente:
        print(f"O serviço {nome} ja esta cadastrado")
    else:
        while True:
            valor = float(input("Valor: "))
            if valor > 0:
                break
            print("O valor deve ser maior que zero.")

        duracao = int(input("Duração (minutos): "))

        servico = Servico(nome, valor, duracao)
        servicos.append(servico)
        #meu_salao.servicos.append(servico)

        print("Serviço cadastrado!\n")

def listar_clientes():
    print("\n=== Clientes ===")

    if not clientes:
    #if not meu_salao.clientes:
        print("Nenhum cliente cadastrado.")
        return

    for i, cliente in enumerate(clientes):
    #for i, cliente in enumerate(meu_salao.clientes):
        print(f"{i+1} - {cliente}") #Se houvesse um RNF falando sobre intuitividade o "i+1" ajuda na visualização por parte do usuario final

def listar_servicos():
    print("\n=== Serviços ===")

    if not servicos:
    #if not meu_salao.servicos:
        print("Nenhum serviço cadastrado.")
        return

    for i, servico in enumerate(servicos):
    #for i, servico in enumerate(meu_salao.servicos):
        print(f"{i+1} - {servico}")#Se houvesse um RNF falando sobre intuitividade o "i+1" ajuda na visualização por parte do usuario final

def agendar():
    print("\n=== Novo Agendamento ===")

    if len(clientes) == 0:
    #if len(meu_salao.clientes) == 0:
        print("Cadastre um cliente primeiro.")
        return

    if len(servicos) == 0:
    #if len(meu_salao.servicos) == 0:
        print("Cadastre um serviço primeiro.")
        return

    listar_clientes()
    indice_cliente = int(input("Escolha o cliente: "))
    if indice_cliente < 1 or indice_cliente > len(clientes):
    #if indice_cliente < 1 or indice_cliente > len(meu_salao.clientes):
        print("Cliente inválido!\n")
        return
    
    listar_servicos()
    indice_servico = int(input("Escolha o serviço: "))
    if indice_servico < 1 or indice_servico > len(servicos):
    #if indice_servico < 1 or indice_servico > len(meu_salao.servicos):
        print("Serviço inválido!\n")
        return
    
    data = input("Data (dd/mm/aaaa): ")
    horario = input("Horário (HH:MM): ")

    # Regra de negócio
    for ag in agendamentos:
    #for ag in meu_salao.agendamentos:
        if ag.data == data and ag.horario == horario:
            print("Já existe um agendamento nesse horário!\n")
            return

    novo = Agendamento(
        clientes[indice_cliente-1],
        #meu_salao.clientes[indice_cliente-1],
        servicos[indice_servico-1],
        #meu_salao.servicos[indice_servico-1],
        data,
        horario
    )

    agendamentos.append(novo)
    #meu_salao.agendamentos.append(novo)

    print("Agendamento realizado!\n")

def listar_agendamentos():
    print("\n=== Agendamentos ===")

    if not agendamentos:
    #if not meu_salao.agendamentos:
        print("Nenhum agendamento.\n")
        return
    for i, agendamento in enumerate(agendamentos):
    #for i, agendamento in enumerate(meu_salao.agendamentos):
        print(f"{i+1} - {agendamento}")

def cancelar_agendamento():
    print("\n=== Cancelar Agendamento ===")

    if not agendamentos:
    #if not meu_salao.agendamentos:
        print("Nenhum agendamento cadastrado.\n")
        return

    listar_agendamentos()

    indice = int(input("Informe o número do agendamento: "))
    indice -=1
    
    if 0 <= indice < len(agendamentos):
    #if 0 <= indice < len(meu_salao.agendamentos):
        agendamentos.pop(indice)
        #meu_salao.agendamentos.pop(indice)
        print("Agendamento cancelado!\n")
    else:
        print("Índice inválido.\n")

def editar_cliente():
    print("\n=== Editar clientes ===")
    
    if not clientes:
        print("Nenhum cliente cadastrado.\n")
        return
    
    listar_clientes()
    indice_cliente = int(input("Escolha o cliente: "))
    if indice_cliente < 1 or indice_cliente > len(clientes):
    #if indice_cliente < 1 or indice_cliente > len(meu_salao.clientes):
        print("Cliente inválido!\n")
        return
    
    cliente = clientes[indice_cliente-1]
    #cliente = meu_salao.clientes[indice_cliente-1]
    print("Forneca agora os novos dados para Edição do cliente")
    cliente.nome = input("Digite o novo Nome: ")
    #meu_salao.cliente.nome = input("Digite o novo Nome: ")
    cliente.telefone = input("Digite o novo telefone: ")
    #meu_salao.cliente.telefone = input("Digite o novo telefone: ")
    cliente.email = input("Digite o novo email: ")
    #meu_salao.cliente.email = input("Digite o novo email: ")
    print(f"Cliene {cliente.nome} atualizado com sucesso \n")
    
    #editar possiveis agendamentos anteriores
    
#meu_salao = SalaoBeleza("Salão Beauty Manager")
#print(f"Bem vindo ao salao {meu_salao.nome_salao}")

while True:

    print("""======== SALÃO DE BELEZA ========
                1 - Cadastrar Cliente
                2 - Cadastrar Serviço
                3 - Agendar Atendimento
                4 - Listar Agendamentos
                5 - Cancelar Agendamento
                6 - Editar Cliente
                0 - Sair
                """)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        cadastrar_servico()

    elif opcao == "3":
        agendar()

    elif opcao == "4":
        listar_agendamentos()

    elif opcao == "5":
        cancelar_agendamento()

    elif opcao == "6":
        editar_cliente()
    elif opcao == "0":
        print("Sistema encerrado.\n")
        break

    else:
        print("Opção inválida.\n")