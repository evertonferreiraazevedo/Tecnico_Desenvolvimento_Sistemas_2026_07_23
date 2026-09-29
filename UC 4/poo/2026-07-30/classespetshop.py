class Pet:
    def __init__(self, nome: str, especie: str, raca: str, idade_anos: int):
        # Atributos privados (__)
        self.__nome = nome
        self.__especie = especie
        self.__raca = raca
        self.__idade_anos = idade_anos

    # Método Público: Calcula e retorna a idade em meses
    def calcular_idade_meses(self) -> int:
        return self.__idade_anos * 12

    # Método Público: Permite corrigir a raça se houver erro
    def atualizar_raca(self, nova_raca: str) -> None:
        if nova_raca.strip():  # Valida se o texto não está vazio
            self.__raca = nova_raca
            print(f"Raça do pet {self.__nome} corrigida para: {nova_raca}.")
        else:
            print("Erro: O nome da raça não pode ser vazio.")

    # Getters públicos para visualização segura
    def get_nome(self) -> str:
        return self.__nome

    def get_raca(self) -> str:
        return self.__raca


class Servico:
    def __init__(self, nome_servico: str, preco_base: float, duracao_minutos: int):
        self.__nome_servico = nome_servico
        self.__preco_base = preco_base
        self.__duracao_minutos = duracao_minutos

    # Método Público: Aplica um desconto em reais
    def aplicar_desconto(self, valor_desconto: float) -> None:
        if 0 < valor_desconto < self.__preco_base:
            self.__preco_base -= valor_desconto
            print(f"Desconto de R$ {valor_desconto:.2f} aplicado no serviço '{self.__nome_servico}'.")
            print(f"Novo valor do serviço: R$ {self.__preco_base:.2f}")
        else:
            print("Erro: Valor de desconto inválido ou maior que o preço base.")

    def get_preco(self) -> float:
        return self.__preco_base


class Veterinario:
    def __init__(self, nome_vet: str, crmv: str, Black: str):
        self.__nome_vet = nome_vet
        self.__crmv = crmv
        self.__especialidade = Black

    # Método Público: Altera a especialidade após novo curso
    def alterar_especialidade(self, nova_especialidade: str) -> None:
        if nova_especialidade.strip():
            self.__especialidade = nova_especialidade
            print(f"O(A) Dr(a). {self.__nome_vet} agora é especialista em: {nova_especialidade}.")
        else:
            print("Erro: A especialidade não pode ser vazia.")

    def get_especialidade(self) -> str:
        return self.__especialidade