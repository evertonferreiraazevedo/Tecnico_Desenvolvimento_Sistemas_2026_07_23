class Veiculo:
    nome_estacionamento = "Shopping Central"
    valor_hora = 8.0
    patio_estacionamento = []

    def __init__(self, placa: str, modelo: str, proprietario: str, horas_estacionadas: float = 0.0):
        self.placa = placa
        self.modelo = modelo
        self.proprietario = proprietario
        self.__horas_estacionadas = horas_estacionadas

    def adicionar_horas(self, horas):
        if horas > 0:
            self.horas_estacionadas += horas
        else:
            print("Quantidade de horas deve ser maior que zero.")

    def calcular_valor_total(self):
        return self.horas_estacionadas * Veiculo.valor_hora

    def exibir_dados(self):
        print(f"\n--- Dados do Veículo ---")
        print(f"Proprietário: {self.proprietario}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Horas Estacionadas: {self.horas_estacionadas}h")

    @classmethod
    def exibir_informacoes_estacionamento(cls) -> None:
        print(f"\n{cls.nome_estacionamento}")
        print(f"Valor da hora: R$ {cls.valor_hora:.2f}")
        print(f"Quantidades de veiculos estacionado: {len(cls.patio_estacionamento)}")

    @classmethod
    def remover_veiculo_patio(cls, veiculo):
        if veiculo in cls.patio_estacionamento:
            cls.patio_estacionamento.remove(veiculo)

    @staticmethod
    def validar_placa(placa):
        placa_limpa = placa.replace("-", "")
        return len(placa_limpa) == 7


        