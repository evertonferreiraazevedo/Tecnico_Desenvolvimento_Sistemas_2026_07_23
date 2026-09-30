from models.aluno_model import carregar_alunos, salvar_alunos

def cadastrar_aluno(nome, idade, curso):
    if not nome:
        return False, "Informe o nome do aluno."
    if not idade:
        return False, "Informe a idade."
    if not curso:
        return False, "Informe o curso."
    try:
        idade = int(idade)
    except ValueError:
        return False, "A idade deve ser um número."
    aluno = {
        "Nome": nome,
        "Idade": idade,
        "Curso": curso
    }

    alunos = carregar_alunos()
    alunos.append(aluno)
    salvar_alunos(alunos)
    return True, "Aluno cadastrado com sucesso!"

def listar_alunos():
    return carregar_alunos()