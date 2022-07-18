# string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
#
# lista = []
# for i in range(0, len(string) - 9, 10):
#     lista.append(string[i:i + 10])
# print('.'.join(lista))
import google

string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
contador = 10
lista = list(string[comeco:comeco + contador]for comeco in range(0, len(string), contador))
string = '.'.join(lista)
print(lista)
print(string)
google