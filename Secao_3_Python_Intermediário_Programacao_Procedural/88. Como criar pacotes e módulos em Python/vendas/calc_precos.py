def aumento(preco_atual, porcentagem_aumento):
    result = preco_atual + (preco_atual * (porcentagem_aumento / 100))
    return result


def reducao(preco_atual, porcentagem_d_reducao):
    result = preco_atual - (preco_atual * (porcentagem_d_reducao / 100))
    return result


if __name__ == '__main__':
    print(aumento(10, 5))
