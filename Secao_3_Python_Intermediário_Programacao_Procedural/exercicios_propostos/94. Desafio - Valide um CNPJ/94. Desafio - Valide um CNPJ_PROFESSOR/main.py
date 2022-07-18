import cnpj
import os
os.system('cls' if os.name == 'nt' else 'clear')

'''
O módulo se chama cnpj, se eu chamar algo aqui dentro de cnpj, vai subistituir o módulo
'''
cnpj1 = "40.688.134/0001-61"


if cnpj.valida(cnpj1):  # se a funçao retornar True:
    print(f'{cnpj1} É válido')
else:
    print(f'{cnpj1} É inválido')


for i in range(100):
    novo_cnpj = cnpj.gera()
    formatado = cnpj.formata(novo_cnpj)
    print(formatado)
# print(cnpj.formata(cnpj1))