import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_DATA = os.path.join(BASE_DIR, "data")
ARQUIVO = os.path.join(PASTA_DATA, "alunos.json")

def carregar_alunos():
    if not os.path.exists(PASTA_DATA):
        os.makedirs(PASTA_DATA)
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, indent=4)
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []

def salvar_alunos(alunos):
    if not os.path.exists(PASTA_DATA):
        os.makedirs(PASTA_DATA)
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            alunos,
            arquivo,
            indent=4,
            ensure_ascii=False )