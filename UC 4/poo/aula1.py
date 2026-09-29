class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.peso = 100
    
    def saudacao(self):
        print(f"Olá meu nome é {self.nome}!")   
pessoa1 = Pessoa("Everton", 31)
pessoa2 = Pessoa("Maria", 33)
pessoa3 = Pessoa("Joao", 27)
pessoa1.saudacao()

# print(pessoa1.nome)

# pessoa = "Everton"
# idade = 31
# pessoa2 = "Maria"
# idade2 = 33
# pessoa3 = "Joao"
# idade3 = 27
