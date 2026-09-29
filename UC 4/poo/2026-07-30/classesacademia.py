class PlanoAssinatura:
    def __init__(self, nome_plano: str, valor_mensalidade: float, duracao_meses: int):
        self.__nome_plano = nome_plano
        self.__valor_mensalidade = valor_mensalidade
        self.__duracao_meses = duracao_meses
    def aplicar_reajuste(self, percentual: float) -> None:
        if percentual > 0:
            self.__valor_mensalidade += self.__valor_mensalidade * (percentual / 100)
    def get_nome_plano(self) -> str:
        return self.__nome_plano
    def get_valor(self) -> float:
        return self.__valor_mensalidade

class Treino:
    def __init__(self, nome_treino: str, nivel_dificuldade: str, qtd_series: int):
        self.__nome_treino = nome_treino
        self.__nivel_dificuldade = nivel_dificuldade
        self.__qtd_series = qtd_series
    def alterar_dificuldade(self, nova_dificuldade: str) -> None:
        self.__nivel_dificuldade = nova_dificuldade
    def get_nome_treino(self) -> str:
        return self.__nome_treino

class Aluno:
    def __init__(self, matricula: int, nome: str, altura: float, peso: float, plano: PlanoAssinatura):
        self.__matricula = matricula
        self.__nome = nome
        self.__altura = altura
        self.__peso = peso
        self.__plano = plano 
        self.__treinos = [] 
    def calcular_imc(self) -> float:
        return self.__peso / (self.__altura ** 2)
    def atualizar_peso(self, novo_peso: float) -> None:
        if novo_peso > 0:
            self.__peso = novo_peso

    def adicionar_treino(self, novo_treino: Treino) -> None:
        self.__treinos.append(novo_treino)
    
    def exibir_perfil(self) -> None:
        print(f"Aluno: {self.__nome}")
        print(f"Plano Contratado: {self.__plano.get_nome_plano()} (R$ {self.__plano.get_valor():.2f})")
        print("Fichas de Treino Ativas:")
        if len(self.__treinos) == 0:
            print(" -> [AVISO] Aluno sem treinos cadastrados!")
        else:
            for t in self.__treinos:
                print(f" -> {t.get_nome_treino()}")






if __name__ == "__main__":
    plano_mensal = PlanoAssinatura("Plano Mensal", 120.0, 1)
    aluno = Aluno(101, "Rodrigo Lima", 1.75, 78.0, plano_mensal)
    treino_a = Treino("Treino A - Peito", "Iniciante", 4)
    treino_b = Treino("Treino B - Costas", "Iniciante", 4)
    
    aluno.adicionar_treino(treino_a)
    aluno.adicionar_treino(treino_b)
    aluno.exibir_perfil()
    aluno.nome