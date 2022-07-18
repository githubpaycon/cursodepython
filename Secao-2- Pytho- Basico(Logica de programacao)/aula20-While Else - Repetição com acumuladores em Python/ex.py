# contador = -1
#
# while contador >= -10:
#     print(contador)
#     contador = contador - 1
#












c = 1  # contador
a = 1  # acumulador

while c <= 10:
    print(c, a, 'acumulador está sendo somado juntamente com o contador')
    a = c + a
    c += 1
else:
    print('Programa finalizado com sucesso!')
contador = 1
acumulador = 1

while contador <= 10:
    acumulador = contador + acumulador
    contador += 1
    print(contador, acumulador)