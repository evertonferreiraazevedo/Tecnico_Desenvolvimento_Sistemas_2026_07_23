class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular       # Público
        self._agencia = "0001"       # Protegido
        self.__saldo = saldo         # Privado
        
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido!")    
        
conta = ContaBancaria("Mariana", 2000)
print(conta.titular)   # Funciona: Mariana
print(conta._agencia)
print(conta.get_saldo()) # ERRO! AttributeError: 'ContaBancaria' object has no attribute '__saldo'


# class Smartphone:
#     def __init__(self, modelo, bateria):
#         self.modelo = modelo
#         self.__bateria = bateria  # Privado (0 a 100)
#      # Cria o "Getter"
#     @property
#     def bateria(self):
#         return f"{self.__bateria}%"
#     # Cria o "Setter" para o mesmo nome
#     @bateria.setter
#     def bateria(self, nova_carga):
#         if 0 <= nova_carga <= 100:
#             self.__bateria = nova_carga
#         else:
#             print("Erro: A carga da bateria deve ser entre 0 e 100!")


# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular       # Público
#         self._agencia = "0001"       # Protegido
#         self.__saldo = saldo         # Privado
# conta = ContaBancaria("Mariana", 2000)
# print(conta.titular) # Funciona: Mariana
# print(conta.__saldo) # ERRO! AttributeError: 'ContaBancaria' object has no attribute '__saldo'

