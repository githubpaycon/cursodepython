"""
Desempacotamento de listas em
            Python
"""
# str = 'Jesus Gabriel João'
# lista = str.split()
#
# n1, n2, n3, n4 = lista  # principio do desempacotamento (syntax)
#
# print(n2)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

*outra_lista, dez, onze, doze = lista

print(outra_lista)