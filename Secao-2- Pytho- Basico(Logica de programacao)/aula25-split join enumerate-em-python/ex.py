"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list. Para objetos iteráveis.
"""

frase = 'O mundo não cumpre a biblia, mas a bíblia se cumpre no mundo.'
list1 = frase.split()
# list2 = frase.split(',')

# para saber quantas vezes uma palavra apareceu mais vezes
palavra = ''  # palavra que foi mostrada mais vezes
contagem = 0
for item in list1:
    qtd_vezes = list1.count(item)

    if qtd_vezes > contagem:  # se a qtd_vezes for maior que a contagem que é 0
        contagem = qtd_vezes  # a váriavel contagem que está fora do laço será atribuida a qtd_vezes que a palavra apareceu
        palavra = item  # a palavra será atribuida ao item que foi contado mais vezes.
print(f'A palavra "{palavra}" apareceu {contagem} vezes"')











# for item in lista_da_frase2:
#     print(item)
# print(lista_da_frase,'\n', lista_da_frase2)
