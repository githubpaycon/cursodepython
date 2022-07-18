def divide(n1, n2):
    if n2 == 0:
        raise ValueError(f'n2 não pode ser 0')
    return n1 / n2


try:
    print(divide(2, 0))
except ValueError as descricao:
    print(descricao)