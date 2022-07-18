# """
# Split, Join, Enumerate em Python
# * Split - Dividir uma string # str
# * Join - Juntar uma lista # str
# * Enumerate - Enumerar elementos da lista # list. Para objetos iteráveis.
# """
#
# frase = 'Ame o seu próximo como a ti mesmo'
#
# lista_da_frase = frase.split()
#
# print('# split ' * 10)  #
#
# for item in lista_da_frase:
#     print(item.capitalize())
# print('#' * 40)
#
# mercearia = 'Arroz, Feijão, Macarrão'
#
# lista_mercearia = mercearia.split(',')
#
# for item in lista_mercearia:
#     print(item.strip())
#
# print('# Join ' * 10)  #
#
# frase2 = 'Ame o seu próximo como a ti mesmo'
# print(frase2)  # antes da modificação
# lista = frase2.split()  # modificando a string em lista
# print(lista)  # lista da string
# frase3 = 'Jesus'.join(lista)  # lista é transformada em string
# print(frase3)  # string que anteriormente era uma lista, usando # na separação das palavras.
#
# listpalavra = ['Jesus', 'é', 'o', 'Senhor']
# palavra = ' SIM '.join(listpalavra)
# print(palavra)

# frase = 'Deus é bom o tempo todo'
# lista_frase = frase.split()
#
# for indice, item in enumerate(lista_frase):
#     print(f'O índice é {indice} e o seu item é: {item} \n {lista_frase[indice]}')

# listas = [
#     ['Gabriel'],
#     ['João'],
#     ['Emilia'],
#     ['Reinaldo'],
#     ['Jesus']
# ]
# for indice, nome in enumerate(listas, 1):
#     print(indice, nome)
nome = 'gabriel'

for indice, letra in enumerate(nome, 1):
    print(indice, letra)

for letra in enumerate(nome, 1):
    print(letra)

lista = [123, 432, 12412, 534523]

for numero, item in enumerate(lista):
    print(numero, item)
else:
    print(len(lista))