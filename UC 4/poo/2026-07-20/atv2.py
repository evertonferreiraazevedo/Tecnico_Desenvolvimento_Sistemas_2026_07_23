class Pessoa:
    especie = "Homo sapiens"

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura 

    def __str__(self):
        return f"\n{self.nome} - Idade: {self.idade} anos \nPeso: {self.peso:.1f} kg\nAltura: {self.altura/100:.2f}m\n"

    @classmethod
    def nascer(cls, nome):
        # Construtor alternativo: cria um bebe padrao com idade 0, peso 3 e altura 50cm
        return cls(nome, 0, 3.0, 50.0)

    @staticmethod
    def calcular_imc(peso, altura_m):
        return peso / (altura_m ** 2)

    def envelhecer(self):
        if self.idade < 21:
            self.crescer(0.5)
        self.idade += 1
        print(f"{self.nome} tem agora {self.idade} ano(s)!")

    def engordar(self):
        self.peso += 3
        print(f"{self.nome} engordou 3 kg!")

    def emagrecer(self):
        self.peso -= 0.5
        print(f"{self.nome} emagreceu 0.5 kg!")

    def crescer(self, centimetros):
        self.altura += centimetros


print("=== SISTEMA DE CADASTRO ===")
print("[1] Cadastrar pessoa manualmente")
print("[2] Registrar nascimento de bebe")
modo = input("Escolha o modo: ")

if modo == "2":
    nome_bebe = input("Digite o nome do bebe: ")
    p = Pessoa.nascer(nome_bebe)
else:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso kg: "))
    altura_m = float(input("Digite a altura (ex: 1.77): "))
    altura_cm = altura_m * 100  
    p = Pessoa(nome, idade, peso, altura_cm)


while True:
    print(p)
    print("[1] Envelhecer")
    print("[2] Engordar")
    print("[3] Emagrecer")
    print("[4] Crescer manualmente")
    print("[5] Consultar Calculadora de IMC")
    print("[6] Sair")
    
    opcao = input("\nEscolha uma opcao: ")

    if opcao == "1":
        p.envelhecer()
    elif opcao == "2":
      #  qnt = float(input("Quantos quilos engordou? "))
        p.engordar()
    elif opcao == "3":
        #qnt = float(input("Quantos quilos emagreceu? "))
        p.emagrecer()
    elif opcao == "4":
        cm = float(input("Quantos centimetros quer crescer? "))
        p.crescer(cm)
        print(f"{p.nome} cresceu {cm} cm!")
    elif opcao == "5":
        imc_atual = Pessoa.calcular_imc(p.peso, p.altura / 100)
        print(f"O IMC atual de {p.nome} eh: {imc_atual:.2f}")
    elif opcao == "6":
        print("FIM")
        break
    else:
        print("Opcao invalida")
