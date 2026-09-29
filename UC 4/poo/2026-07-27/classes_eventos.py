from abc import ABC, abstractmethod

class Eventos(ABC):
    lista_eventos = []
    def __init__(self, local, data, capacidade, ingresso):
        self.local = local
        self.data = data
        self.capacidade = capacidade
        self.ingresso = ingresso
        self.lista_participantes = []
        self.disponivel = True
        self.ingresso_vendido = 0
        Eventos.lista_eventos.append(self)
    
    def __str__(self):
        return f"Local: {self.local} | Data: {self.data} | Disponível: {self.disponivel}"
    
    @classmethod
    def verificar_eventos_disponiveis(cls):
        encontrou_evento = False 
        for evento in cls.lista_eventos:
            if evento.disponivel == True:
                print(evento)
                encontrou_evento = True
                
        if encontrou_evento == False:
            print("Nenhum evento disponível no momento.")
    
    @abstractmethod            
    def valor_comissao(self):   
        pass
    
    def vender_ingresso(self, pessoa):
        if self.ingresso_vendido < self.capacidade and self.disponivel == True:
            self.lista_participantes.append(pessoa)
            self.ingresso_vendido += 1
            if self.ingresso_vendido == self.capacidade:
                self.disponivel = False
            print(f"Ingresso vendido com sucesso para {pessoa.nome}!")
        else: 
            self.disponivel = False
            print(f"Erro: Capacidade máxima de {self.capacidade} pessoas atingida ou evento indisponivel")
            
class Show(Eventos):
    def valor_comissao(self):
        return self.ingresso * 0.10

class Festa(Eventos):
    def valor_comissao(self):
        return self.ingresso * 0.05

class Palestra(Eventos):
    def valor_comissao(self):
        return self.ingresso * 0.25

class Feiras(Eventos):
    def valor_comissao(self):
        return self.ingresso * 0.15
    
class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Participante(Pessoa):
    pass
