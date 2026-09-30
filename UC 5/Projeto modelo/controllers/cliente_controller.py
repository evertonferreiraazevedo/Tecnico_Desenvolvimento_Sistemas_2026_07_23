import re

from models.cliente_model import (
    carregar_clientes,
    salvar_clientes
)


def validar_email(email):
    if not email:
        return True

    padrao = r"^[\w\.-]+@[\w\-]+\.[a-zA-Z]{2,}$"

    return re.match(
        padrao,
        email
    ) is not None


def validar_telefone(telefone):

    padrao = r"^(\(\d{2}\)\s?)?\d{4,5}-?\d{4}$"

    return re.match(
        padrao,
        telefone
    ) is not None


def cadastrar_cliente(
    nome,
    sobrenome,
    telefone,
    endereco,
    email
):

    if not nome or not sobrenome or not telefone:

        return False, "Campos obrigatórios não preenchidos."

    if not validar_email(email):

        return False, "E-mail inválido."

    if not validar_telefone(telefone):

        return False, "Telefone inválido."

    novo_cliente = {
        "Nome": nome,
        "Sobrenome": sobrenome,
        "Telefone": telefone,
        "Endereço": endereco if endereco else "Não informado",
        "Email": email
    }

    lista_clientes = carregar_clientes()

    lista_clientes.append(novo_cliente)

    salvar_clientes(lista_clientes)

    return True, "Cliente cadastrado com sucesso!"


def excluir_cliente(cliente):

    lista_atual = carregar_clientes()

    lista_nova = []

    for cliente_atual in lista_atual:

        if (
            cliente_atual["Nome"] == cliente["Nome"]
            and
            cliente_atual["Telefone"] == cliente["Telefone"]
        ):
            continue

        lista_nova.append(cliente_atual)

    salvar_clientes(lista_nova)