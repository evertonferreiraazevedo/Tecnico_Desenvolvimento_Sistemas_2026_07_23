# class Cliente:

#     def __init__(self, nome, cpf):
#         self.nome = nome
#         self.cpf = cpf


# cliente1 = Cliente("Maria", "111.111.111-11")
# cliente2 = Cliente("Carlos", "222.222.222-22")

# print(cliente1.nome) #saida “Maria”
# # print(cliente2.nome) #saida “Carlos”
# class Aluno:
#     escola = "Senac"
#     contador_alunos = 0 
#     def __init__(self, nome):
#         self.nome = nome
#         Aluno.contador_alunos += 1
#         print(f"Aluno {self.nome} Criado com sucesso, agora temos: {Aluno.contador_alunos} Alunos!")
# aluno1 = Aluno("Pedro")
# aluno2 = Aluno("Ana")
# Aluno.escola = "Senac Centro"
# aluno3 = Aluno("Everton")
# print(aluno1.escola)
# print(aluno2.escola)
# # print(aluno3.escola)
# class Conta:

#     def __init__(self, saldo):
#         self.saldo = saldo
#     def depositar(self, valor):
#         self.saldo += valor
# conta = Conta(100)
# conta2 = Conta(665)
# conta.depositar(10)
# print(conta.saldo)
# print(conta2.saldo)
# class ContaBancaria:
#     total_contas_criadas = 0  # Atributo de classe

#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#         ContaBancaria.total_contas_criadas += 1

#     # MÉTODO DE CLASSE: Usa 'cls' em vez de 'self'
#     @classmethod
#     def exibir_total_contas(cls):
#         # Ele acessa o atributo de classe diretamente através do 'cls'
#         print(f"Total de contas no banco atualmente: {cls.total_contas_criadas}")

# # Uso na prática (Não precisamos criar uma conta para chamar o método!)
# ContaBancaria.exibir_total_contas()  # Saída: 0

# conta1 = ContaBancaria("João", 500)
# ContaBancaria.exibir_total_contas()  # Saída: 1
class Calculadora:

    @staticmethod
    def somar(a, b):
        return a + b
    @classmethod
    def subtrair(cls, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b

print(Calculadora.somar(10, 5))
print(Calculadora.subtrair(10, 5))
calc = Calculadora()
print(calc.multiplicar(10, 5))
