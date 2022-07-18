lista = [
    ('Nome', 'Gabriel'),
    ('Sobrenome', 'Lopes'),
]


def cria_dict_range_elevar(elevador, tam_range):
    return {f'Chave_{x}': x ** elevador for x in range(tam_range)}


def cria_dict_enumerate(tamanho_range):
    return {x: y for x, y in enumerate(range(tamanho_range))}


def cria_set_range(taman_range):
    return {num for num in range(taman_range)}


print(cria_dict_range_elevar(2, 6))
print(cria_dict_enumerate(6))
print(cria_set_range(15))
