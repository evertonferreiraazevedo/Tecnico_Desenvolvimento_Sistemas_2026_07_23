# #petshop
# #superClasse
# class Pessoa:
#     def __init__(self, nome, cpf):
#             self.nome = nome
#             self.cpf = cpf
            
# class Cliente(Pessoa):
#     pass
# class Fornecedor(Pessoa):
#     pass
# class Veterinario(Pessoa):
#     pass

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome
    @abstractmethod
    def falar(self):
        return "au au"
    
class Cachorro(Animal):
    def __init__(self, nome, especie):
        super().__init__(nome)
        self.especie = especie
        
    def falar(self):
        return 

class Gato(Animal):
    def falar(self):
        return "Miau!"

# Uso da herança
animais = [Cachorro("Rex", "Cachorro"), Gato("Whiskers")]

for animal in animais:
    print(f"{animal.nome} diz {animal.falar()}")



