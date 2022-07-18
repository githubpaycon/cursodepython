# def func(arg, arg2):
#     return arg * arg2
#
#
# print(func(2, 4))

lista = [['Arroz', 12], ['Bisteca', 11], ['Acem', 121], ['Macarrão', 3],
         ['Feijão', 6]]  # lista de itens do mercado com seus valores

print(sorted(lista, key=lambda item: item[1]))
# mostra a lista, e usa lambda que faz: na lista 0 acesse o item 1 (que é o preço)
# e ordena conforme do mais baixo p/ o mais alto
