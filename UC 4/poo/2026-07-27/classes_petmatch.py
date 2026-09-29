from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        print(f"{self.nome}, cadastrado")

    def __str__(self):
        return f"{self.nome} é um {self.raca} de {self.idade} anos"

    @abstractmethod
    def emitir_som(self):
        pass

    def comer(self):
        return f"{self.nome} está comendo"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au Au"

class Cobra(Animal):
    def emitir_som(self):
        return "shhh shhhh"

class Coelho(Animal):
    def emitir_som(self):
        return "Sniff Sniff"

class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Tutor(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.lista_animais = []
        print(f"{self.nome}, cadastrado")

    def adicionar_animal(self, animal):
        self.lista_animais.append(animal)
        return f"{animal.nome} adicionado ao tutor {self.nome}."

    def listar_animais(self):
        if not self.lista_animais:
            print(f"{self.nome} não possui animais cadastrados.")
        for animal in self.lista_animais:
            print(f"- {animal}")
            
class Participante(Pessoa):
    pass

class Encontro:
    def __init__(self, nome_parque, data):
        self.nome_parque = nome_parque
        self.data = data
        self.animais_inscritos = []

    def inscrever_animal(self, animal):
        if animal not in self.animais_inscritos:
            self.animais_inscritos.append(animal)
            print(f"{animal.nome} inscrito no encontro do {self.nome_parque}!")
        else:
            print(f"{animal.nome} já está inscrito neste encontro.")

    def cancelar_inscricao(self, animal):
        if animal in self.animais_inscritos:
            self.animais_inscritos.remove(animal)
            print(f"Inscrição de {animal.nome} cancelada.")
        else:
            print(f"Erro: {animal.nome} não estava inscrito neste encontro.")

    def exibir_inscritos(self):
        print(f"\nAnimais Inscritos: {self.nome_parque} ({self.data})")
        if not self.animais_inscritos:
            print("Nenhum animal inscrito até o momento.")
            return
        for animal in self.animais_inscritos:
            print(f"-> {animal} | Som: {animal.emitir_som()}")

tutor1 = Tutor("Carlos Silva", "123.456.789-00")
tutor2 = Tutor("Ana Souza", "987.654.321-11")

cachorro = Cachorro("Rex", "Golden", 3)
gato = Gato("Mingau", "Persa", 2)
cobra = Cobra("Pompom", "Cascavel", 1)

tutor1.adicionar_animal(cachorro)
tutor1.adicionar_animal(gato)
tutor2.adicionar_animal(cobra)

encontro_parque = Encontro("Parque do Cocó", "30/07/2026")

encontro_parque.inscrever_animal(cachorro)
encontro_parque.inscrever_animal(cobra)

encontro_parque.exibir_inscritos()

encontro_parque.cancelar_inscricao(cachorro)
encontro_parque.exibir_inscritos()