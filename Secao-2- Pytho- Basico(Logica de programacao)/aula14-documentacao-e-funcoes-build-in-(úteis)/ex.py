# .isnumeric() identifica se o que o usuário digitou pode ser convertido em número
# PODE USAR AS FUNÇÕES DO PROFESSOR ABAIXO

import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

# is_number(variavel) é usado para saber se o que o usuário digitou é um número inteiro(int) ou real(float)
# ou se é positivo ou negativo
def is_number(val):
    return is_int(val) or is_float(val)

# PODE USAR AS FUNÇÕES DO PROFESSOR ACIMA


n2 = input('Digite um número: ')
n1 = input(f'Digite outro número: ')

if not is_number(n1) and not is_number(n2):
    print('Não é um número, tente novamente.')
elif is_number(n2) and is_number(n2):
    n1 = float(n1)
    n2 = float(n2)
    soma = n1 + n2
    print(f'A soma entre {n1} e {n2} é {soma}')

"""
.isnumeric -> identifica somente se o que o usuário digitou é um número inteiro e positivo.
caso seja ele retorna True, senão False


"""
