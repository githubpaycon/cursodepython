# add uma lista em outra usando list comprehension
lnum = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # lista normal

lista2 = ['Gabriel', 'João', 'Reinaldo']

tupla = (
    ('Nome', 'Gabriel'),
    ('Salvador', 'Jesus')
)
lista_grande_numeros = range(100)


def inverte_chave_valor(iter_c_v):
    return [(x, y) for y, x in iter_c_v]


def verlista(lista):
    return [i for i in lista]
    # para cada numero em l1, adicione na variavel (que está no começo da lista)


def multiplica_por_2_list(lista):
    return [numero * 2 for numero in lista]
    # para cada valor em lista, multiplique o valor por 2 e adicione o resultado na lista do retorno


def cria_cordenadas(lista, tam_cordenada_num=1):
    return [(valor1, valor2) for valor1 in lista for valor2 in range(tam_cordenada_num)]
    # no valor, para cada valor na l1, adiciona o número na variavel valor que está dentro de uma tupla,
    # no valor2, para cada novo número(valor2) que vem do range, adiciona na variável valor2 que está dentro da tupla
    # o segundo for do range, itera sobre cada número da lista até a quantidade do range ser atingida (0, 1, 2)  que é 3


def muda_carac_str_from_list(lista, l_atual, l_pos):
    return [valor.replace(l_atual, l_pos) for valor in lista]
    # para cada valor em lista2, pegue o valor e troque o a por @ e coloque na lista


def ver_divisiveis_por_3_e_8(lista):
    return [num for num in lista if num % 3 == 0 and num % 8 == 0]

def divisiveis_por_3(lista):
    return [num if num % 3 == 0 else 'Não é' for num in lista]


print(divisiveis_por_3(lista_grande_numeros))
print(ver_divisiveis_por_3_e_8(lista_grande_numeros))
print(muda_carac_str_from_list(lista2, 'a', 'b'))
print(verlista(lnum))
print(multiplica_por_2_list(lnum))
print(cria_cordenadas(lnum, 3))
print(inverte_chave_valor(tupla), '|||', tupla)
