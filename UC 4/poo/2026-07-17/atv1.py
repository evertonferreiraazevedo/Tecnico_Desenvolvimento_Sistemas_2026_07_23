class Bola:
    formato = "Esférico"

    def __init__(self, cor, circunferencia):
        self.cor = cor
        self.circunferencia = circunferencia

    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
        
    def mostrar_cor(self):
        return f"A cor é {self.cor}"
    
    @classmethod
    def formato_bola(cls, novo_formato):
        formato = novo_formato
        
    def calcular_diametro(self):
        return self.circunferencia / 3.14

bola = Bola("preta", 10)
diametro = bola.calcular_diametro()
print(diametro) 

Bola.formato_bola("Quadrada")
print(bola.formato)