# """
# Listas em Python
# Fatiamento
# append, insert, pop, del, clear, extend, +
# min, max
# range
# ### MAIS INFORMAÇÕES NO CADERNO DE ESTUDO ###
# """
# # indice  0    1    2    3    4
# lista = ['a', 'b', 'c', 'd', 'e']
# # neg    -5   -4   -3   -2   -1
#
# print(lista)  # mostrando toda a lista na tela
# print(lista[2])  # mostrando um determinado elemento na tela, no caso o 'c'
#
# # alterando um elemento
# lista[2] = 'cabeça'  # o elemento do índice 2 está sendo reatribuido, à 'cabeça'
# print(lista[2])  # Aqui está sendo mostrado na tela o valor do elemento já reatribuido
# print(lista)  # Aqui está sendo mostrado na tela toda a lista, mas com um novo elemento
# # alterando um elemento
#
# print(lista[2:5])  # Aqui está sendo mostrado na tela uma parte dos itens da lista
# print(lista[2:])  # Aqui será mostrado, do 2º item até o último da lista
# print(lista[:3])  # Aqui será mostrado, do 2º item até o último da lista
# print(lista[-1])  # Aqui será mostrado, o último item da lista
# print(lista[0])  # Aqui será mostrado, o primeiro item da lista
# print(lista[::2])  # Aqui será mostrado item sim item não, ou seja, do começo ao final da lista pulando de 2 em 2 itens(step)
#
# print(lista[::-1])  # Aqui será mostrado a lista de trás para frente, (invertendo lista) como um nome, ex: gabriel, leirbag
# nome = 'gabriel'
# print(nome[::-1])
#
#
#
# # nome = 'Gabriel'
# # lista_vazia = []
# # lista_diversificada = [1, 1.22, -12, -1.321, True, False, 'S', 'STR', ['LISTA', 1, 'DENTRO', 1.44, 'DE', True, 'lISTA'],
# #                        nome, print(nome), lista_vazia, '1' == 1,  ...]
# #
# # print(lista_diversificada)
#
# listan = [1,2,3,4,5,6,7]
# print(listan[2])
#
# print(f'{"#"*10} Funções para Listas {"#"*10}')
#
# print("#"*10,'extend()', "#"*10)
# print()
# # Lista de Linguagens
# linguagens = ['Francês', 'Inglês']
#
# # Outra Lista de Linguagens
# outra_lista_de_linguagens = ['Espanhol', 'Português']
#
# # Anexando elementos da lista outra_lista_de_linguagens na lista linguagens mais infos - https://www.programiz.com/python-programming/methods/list/extend
# linguagens.extend(outra_lista_de_linguagens)
#
#
# print('Lista total de linguagens do site:', linguagens)
# print()
# print("#"*10,'extend()', "#"*10)
# print()
# print("#"*10,'append()', "#"*10)
# animais = ['Gato', 'Cachorro', 'Coelho']
#
# print('Lista de animais antiga:', animais)
#
# animais.append('Peixe')
#
# print('Lista de animais atualizada:', animais)
# print()
# print("#"*10,'append() com listas em listas', "#"*10)
#
# animais_domesticos = ['Gato', 'Cachorro', 'Coelho', 'Peixe']
# animais_selvagens = ['Tigre', 'Raposa', 'Elefante']
#
# print('Lista somente de animais domésticos:', animais_domesticos)
# animais_domesticos.append(animais_selvagens)
# print('Lista de animais selvagens dentro da lista de animais domésticos:', animais_domesticos)
#
# print()
# print("#"*10,'append()', "#"*10)
# print()
# print("#"*10,'insert()', "#"*10)
#
# lista = [1, 2, 3, 4, 5]
#
# lista.insert(3, 'Terceiro elemento')
# print(lista)
#
#
#
# print()
# print("#"*10,'insert()', "#"*10,)
#
#



# lista = [1, 2, 3, 4, 5, 6, 7]
#
# # retorno_funcao = lista.pop(-3)
#
# # del lista[1:4]
#
# print(max(lista))
# print(min(lista))
#
# lista2 = list(range(1,10))
# print(lista2)

# lista = ['str', True, 10, -10.5, [1, 2, 3], {1, 2, 3}, (1, 2, 3)]
#
# for item in lista:  # para o item da lista
#     print(f'O tipo primitivo do item é {type(item)}, e o seu valor é {item }')  # mostre na tela o tipo de cada item
#



palavra_secreta = 'água'

letras_corretas = []

while True:
    print('@'*30)
    letra = input('Digite uma letra: ')
    if len(letra) == 1:  # se a letra for igual a 1 letra
        if letra in palavra_secreta:  # se a letra existir na palavra secreta
            print(f'Acertou! A letra "{letra}" existe na palavra!')
            letras_corretas.append(letra)  # está sendo adicionado a letra que o usuario acertou na lista de acertos
            print()
            print(f'As letras que você acertou são essas: {letras_corretas}')
        else:
            print(f'Errou! A letra "{letra}" não existe na palavra!')
            continue
    else:
        input('Por favor, adicione somente uma letra.')
        continue





