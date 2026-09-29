class Quadrado:
    tipo = "Quadrado"

    def __init__(self, lado_inicial):
        self.lado = lado_inicial

    @staticmethod
    def calcular_area(valor_do_lado):
        return valor_do_lado * valor_do_lado

area_avulsa = Quadrado.calcular_area(5)
print(area_avulsa)  

obj_quadrado = Quadrado(10)
print(Quadrado.calcular_area(obj_quadrado.lado)) 
