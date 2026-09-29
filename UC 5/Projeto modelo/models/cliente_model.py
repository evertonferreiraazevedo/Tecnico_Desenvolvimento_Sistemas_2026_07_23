import json
import os

# Caminho da pasta do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Pasta onde os dados ficarão
PASTA_DATA = os.path.join(BASE_DIR, "data")

# Arquivo JSON
ARQUIVO = os.path.join(PASTA_DATA, "clientes.json")


def carregar_clientes():
    # Cria a pasta data caso ela não exista
    if not os.path.exists(PASTA_DATA):
        os.makedirs(PASTA_DATA)

    # Cria o arquivo JSON caso ele não exista
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, indent=4)

        return []

    # Carrega os clientes
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_clientes(lista_clientes):
    # Garante que a pasta exista
    if not os.path.exists(PASTA_DATA):
        os.makedirs(PASTA_DATA)

    # Salva os clientes
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            lista_clientes,
            arquivo,
            indent=4,
            ensure_ascii=False
        )