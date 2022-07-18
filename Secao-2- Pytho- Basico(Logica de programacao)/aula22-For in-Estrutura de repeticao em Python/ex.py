"""
For in em Python
Iterando str com for
função range(start=0, stop, step=1)
"""
# o laço while não é recomendado para fazer esse tipo de processamento com dados de string finitas ou quando sei
# onde termina

# palavra = 'Python'
# c = 0
# while c < len(palavra):
#     print(palavra[c])
#     c += 1

# o laço while não é recomendado para fazer esse tipo de processamento com dados de string finitas ou quando sei
# onde termina

# palavra = 'Olá'
#
# for letra in palavra:
#     print(letra)  # será mostrado uma letra em cada linha

# frutas = ['', 'Laranja', 'Morango', 'Pera']
#
# for fruta in frutas:  # a variável criada "fruta" é o iterador
#     print(fruta)  # mostrará cada fruta na tela
#
# n = 0
# while n <= len(frutas):
#     if frutas == '':
#         continue
#     n += 1
#     print(f'A {n} fruta é: {frutas[n]}')
#     if n == len(frutas):
#         break

# list = list(range(10))


# Salvador = 'Jesus'
# Salvador1 = len(Salvador)
# print(list(Salvador))

# for num in range(1, 10):
#     print(num)

# for num in range(20, 10, -1):
#     print(num)

print(list(range(10, -10, -1)))

for i in range(0, 11, 2):  # Sabendo a tabuada do 2
    print(i)
print('#'*33)
for i in range(0, 20, 3):  # Sabendo a tabuada do 2
    print(i)
print('#'*33)

nome_sobre_todo_nome = 'Jesus'

Nome_Sobre_Todo_Nome = ''

for letra in nome_sobre_todo_nome:
    if letra == 'e' or letra == 'u':
        letra.upper()
        Nome_Sobre_Todo_Nome += letra.upper()
    else:
        Nome_Sobre_Todo_Nome += letra
print(Nome_Sobre_Todo_Nome)

print('# $'*33)
