def calcular_subtotal(quantidade, valor):
    try:
        qtd = float(quantidade.replace(",", "."))
        preco = float(valor.replace(",", "."))

        return qtd * preco

    except (ValueError, AttributeError):
        return 0


def calcular_total(servicos):
    total = 0

    for quantidade, valor in servicos:
        total += calcular_subtotal(
            quantidade,
            valor
        )

    return total