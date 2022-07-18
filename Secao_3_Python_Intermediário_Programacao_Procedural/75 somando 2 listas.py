# forma 1
list1 = [1,2,3,4,5,6,7,8]
list2 = [1,2,3,4,5,6,7,8]

lista_soma = [n1 + n2 for n1, n2 in zip(list1, list2)]
# soma o n1 e n2 da junção das 2 listas

print('Forma 1:', lista_soma)
# forma 1

# forma 2
lista_junta = zip(list1, list2)

lista_somada = [n1 + n2 for n1, n2 in lista_junta]
print('Forma 2:', lista_somada)
# forma 2
