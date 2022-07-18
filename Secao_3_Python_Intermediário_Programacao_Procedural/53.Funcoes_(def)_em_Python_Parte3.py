# """
# Funções - def em python pt3 - *args **kwargs
# """
#
#
# def nome_carros(Marca, *Nomes):  # *args (*names) é utilizado para empacotar os argumentos
#     print(f'Marca: {Marca}')  #
#
#     for nome in Nomes:
#         print(f'Nome: {nome}')
#     else:
#         print(f'Existe {len(Nomes)} nomes de carros nesta lista.')
#
#
# nome_carros('Ford', 'Focus', 'Ecosport', 'Ka', 'F100', 'Fiesta')
#
# nome_carros('Porshe', 911, 718, 'Panamera')
# print()


def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'])


func(1, 312, 4, 1, 1, nome='Gabriel')
