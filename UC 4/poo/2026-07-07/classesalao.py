class Cliente:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome} - {self.telefone}"

class Servico:
    def __init__(self, nome, valor, duracao):
        self.nome = nome
        self.valor = valor
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - R$ {self.valor:.2f} ({self.duracao} min)"

class Agendamento:
    def __init__(self, cliente, servico, data, horario):
        self.cliente = cliente
        self.servico = servico
        self.data = data
        self.horario = horario

    def __str__(self):
        return (f"Cliente: {self.cliente.nome} | "
                f"Serviço: {self.servico.nome} | "
                f"Data: {self.data} | "
                f"Horário: {self.horario}")


# class SalaoBeleza:
#     def __init__(self, nome_salao):
#         self.nome_salao = nome_salao
#         self.clientes = []
#         self.servicos = []
#         self.agendamentos = []

#     def cadastrar_cliente(self, cliente):
#         self.clientes.append(cliente)
        
#     def listar_clientes(self):
#         for c in self.clientes:
#             print(c)