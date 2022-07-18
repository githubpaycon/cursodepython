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


def is_number(var):
    return is_int(var) or is_float(var)

# PODE USAR AS FUNÇÕES DO PROFESSOR ACIMA


print('')  # Quebra de linha
n1 = input('Digite um número e eu saberei se é PAR ou IMPAR: ')

if is_number(n1):
    n1 = int(n1)  # na função de conversão de tipos, tem que colocar a variável dentro da função!
    if n1 % 2 == 0:
        print(f'O número {n1} é PAR')
    else:
        print(f'O número {n1} é IMPAR')
else:
    print(f'O valor {n1} é inválido')
