"""
Manipulando Strings
* String indices
* Fatiamento de Strings [inicio:fim:passo]
* Funções built-in: len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Mais em
https://docs.python.org/3/library/stdtypes.html (Tipos built-in)
https://docs.python.org/3/library/functions.html (Funções built-in ex: len() )
"""

# indices positivos
texto = 'Python js'  # Cada caractere de string tem um indíce esse tem 8 indices

# ex:[012345678] indice da string abaixo INCLUSIVE O ESPAÇO
# ex: python js

print(texto[2]) # assim mostrará somente o "t"
print(texto[8]) # assim mostrará somente o "s"
print(texto[6]) # assim mostrará somente o " "
# print(texto[9]) # Esse vai dar erro porque não existe o indice chamado

# indices negativos começa do -1 para tras

texto2 = 'python js'

#   [-987654321] indice da string abaixo INCLUSIVE O ESPAÇO
# ex: python js

# o de negativo é usado mais para strings longas como uma url
url = 'www.google.com.br/'
# o de negativo é usado mais para strings longas como uma url
# para remover a / pode-se usar a indexação em modo negativo
print(url[:-1])
#
num = 'gabriel'
print(num[4])  # vai mostrar só o 'i'
print(num[-3])  # vai mostrar só 'i'
# python
print(texto[2:7])  # vai mostrar 'thon'
print(texto[:6])  # vai mostrar 'Python'
print(texto[7:])  # mostra somente o js

shark = 'SAMMY SHARK!'
print(shark[6:11:1])  # é o mesmo que shark[6:11] só com o parâmetro de stride (deslocamento)
print(shark[6:11:2])  # é o mesmo que shark[6:11] só com o parâmetro de stride (deslocamento)
print(shark[:12:2])  # é o mesmo que shark[6:11] só com o parâmetro de stride (deslocamento)
