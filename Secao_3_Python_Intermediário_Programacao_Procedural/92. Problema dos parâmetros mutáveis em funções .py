def lista_clientes(clientes_iter_list, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iter_list)
    return lista

lista_clientes1_l = ['fabricio']
lista_clientes1 = lista_clientes(['joao', 'maria', 'eduardo'], lista_clientes1_l)
lista_clientes2 = lista_clientes(['marcos', 'jonas', 'zico'])
lista_clientes3 = lista_clientes(['Jose'])
print(lista_clientes1)
print(lista_clientes2)
print(lista_clientes3)
