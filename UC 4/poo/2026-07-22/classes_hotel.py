class Quarto:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponivel = True

class Hotel:
    quartos_cadastrados = []

    @classmethod
    def adicionar_quarto(cls, quarto):
        cls.quartos_cadastrados.append(quarto)
        print(f"Quarto {quarto.numero} ({quarto.tipo}) adicionado ao hotel com sucesso.")

    @staticmethod
    def verificar_disponibilidade(tipo_procurado) :
      
        for quarto in Hotel.quartos_cadastrados:
            if quarto.tipo == tipo_procurado and quarto.disponivel:
                return True
        return False

    def reservar_quarto(self, quarto):
        if quarto.disponivel:
            quarto.disponivel = False
            print(f"O quarto {quarto.numero} foi reservado.")
        else:
            print(f"O quarto {quarto.numero} já está ocupado.")

    def liberar_quarto(self, quarto: Quarto):
        if not quarto.disponivel:
            quarto.disponivel = True
            print(f"O quarto {quarto.numero} agora está livre.")
        else:
            print(f"O quarto {quarto.numero} já estava disponível.")
