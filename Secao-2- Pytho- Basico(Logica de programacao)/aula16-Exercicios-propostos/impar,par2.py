# PODE USAR AS FUNÇÕES DO PROFESSOR ABAIXO

import re


def is_float(var):
    if isinstance(var, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', var): return True

    return False


def is_int(var):
    if isinstance(var, int): return True
    if re.search(r'^\-{,1}[0-9]+$', var): return True

    return False

# is_number(variavel) é usado para saber se o que o usuário digitou é um número inteiro(int) ou real(float)
# ou se é positivo ou negativo usado também para saber se é possível converte-ló em int


def is_number(var):
    return is_int(var) or is_float(var)

# PODE USAR AS FUNÇÕES DO PROFESSOR ACIMA


n1 = input('Digite um número inteiro e positivo: ')

if n1.isdigit():
    n1 = int(n1)
    n1 = n1 % 2
    if n1 == 0:
        print('Par')
    else:
        print('Impar')
else:
    print('O valor digitado é inválido')