'''
count - iteradores infinitos - Itertools
'''
from itertools import count

contador = count()

#  CONTAR DE 0 A 4 USANDO NEXT() E COUNT()
#
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))

# CRIANDO UM LOOP INFINITO COM COUNT()
# for numero in contador:
#     print(numero)
#

# # CRIANDO UM LOOP DE 0 A 10 USANDO COUNT()
# for num in contador:
#     print(num)
#     if num == 10:
#         break

# contar com decimais no step=..
# from itertools import count
# contador = count(start=9, step=0.1)
# for n in contador:
#     print(round(n, 2))
#     if n >= 10:
#         break

# contar de traz para frente / 10 ao 0
# from itertools import count
# contador = count(start=10, step=-1)
# for n in contador:
#     print(round(n, 2))
#     if n <= 0:
#         break

# FAZENDO CONTADOR COM COUNT()
# from itertools import count
# contador = count(start=1)
#
# nomes = ['Jesus', 'Gabriel', 'João', 'Emilia', 'Reinaldo', 'Irineu']
# nomes_link = zip(nomes, contador)
#
# for nome, indice in nomes_link:
#     print(f'{indice}º {nome}')


# FAZENDO CONTADOR COM WHILE
contador = 1

nomes = ['Jesus', 'Gabriel', 'João', 'Emilia', 'Reinaldo', 'Irineu']

while contador < len(nomes):
    for nome in nomes:
        print(f'{contador}º {nome}')
        contador += 1