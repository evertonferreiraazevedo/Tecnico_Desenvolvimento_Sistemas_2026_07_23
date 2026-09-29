from abc import ABC, abstractmethod
#super classe funcionario
class Funcionario(ABC):
    def __init__(self, cpf, nome, matricula, salario_basico):
        self.cpf = cpf
        self.nome = nome
        self.matricula = matricula
        self.salario_basico = salario_basico

    @abstractmethod
    def calcular_salario(self):
        return self.salario_basico
    
class Vendedor(Funcionario):
    def __init__(self, cpf, nome, matricula, salario_basico, comissao):
        super().__init__(cpf, nome, matricula, salario_basico)
        self.comissao = comissao
        self.vendas = {} #chave:valor sendo a chave "DATA":"ACUMULADO DE VENDAS"
    
    def calcular_salario(self, data_salario):
        if data_salario in self.vendas:
            venda_mes = self.vendas[data_salario]
        else:
            venda_mes = 0
        return self.salario_basico + (venda_mes * self.comissao)
    
    def add_venda(self, valor_venda, data):
    #MM/AAAA
        if data not in self.vendas:
            self.vendas[data] = 0
        self.vendas[data] += valor_venda
        

class Gerente(Funcionario):
    def __init__(self, cpf, nome, matricula, salario_basico, bonus):
        super().__init__(cpf, nome, matricula, salario_basico)
        self.bonus = bonus
    
    def calcular_salario(self):
        return self.salario_basico * self.bonus
    
class Estagiario(Funcionario):
    def __init__(self, cpf, nome, matricula, salario_basico, carga_horaria):
        super().__init__(cpf, nome, matricula, salario_basico)
        self.carga_horaria = carga_horaria
    
    def calcular_salario(self):
        return super().calcular_salario()

class Motorista(Funcionario):

    def calcular_salario(self):
        return super().calcular_salario()