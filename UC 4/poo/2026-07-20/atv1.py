class Retangulo: 
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
        
    def __str__(self):
        return f"Valor da base: {self.ladoA}, valor da altura: {self.ladoB}"
    
    def mudar_lado(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB
    
    @staticmethod
    def calc_area(ladoA, ladoB):
        return ladoA * ladoB
    def calc_perimetro(self):
        return self.ladoA * 2 + self.ladoB * 2
    
ladoa = float(input("Digite o valor da Base"))
ladob = float(input("Digite o valor da Altura"))
retangulo = Retangulo(ladoa, ladob)
print(f"""Info do seu terreno: {retangulo}, 
      area {Retangulo.calc_area(retangulo.ladoA, retangulo.ladoB)}, perimetro {retangulo.calc_perimetro()}""")