from abc import ABC, abstractmethod

class Veiculos(ABC):
    def __init__(self, placa, marca, modelo, ano_fabricacao, custo_basico):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.custo_basico = custo_basico
    
    @abstractmethod
    def calcular_viagem(self):
        pass
    
class Onibus(Veiculos):
    def __init__(self, placa, marca, modelo, ano_fabricacao, custo_basico):
        super().__init__(placa, marca, modelo, ano_fabricacao, custo_basico)
        self.capacidade_maxima = 38
        self.passageiros = 0
    
    def calcular_viagem(self):
        return self.passageiros * self.custo_basico

class Caminhao(Veiculos):
    def __init__(self, placa, marca, modelo, ano_fabricacao, custo_basico):
        super().__init__(placa, marca, modelo, ano_fabricacao, custo_basico)
        self.capacidade_maxima_carga = 10000
        self.peso_carga = 0
            
    def calcular_viagem(self):
        return self.peso_carga * self.custo_basico
    
class Taxi(Veiculos):
    def __init__(self, placa, marca, modelo, ano_fabricacao, custo_basico, bandeira):
        super().__init__(placa, marca, modelo, ano_fabricacao, custo_basico)
        self.km_rodados = 0
        self.bandeira = bandeira
            
    def calcular_viagem(self):
        return self.bandeira + self.custo_basico * self.km_rodados
    
onibus = Onibus("pme-8060", "Mercedes", "sedã", 2030, 4.5,)
print(onibus)