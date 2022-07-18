"""
Operador Ternário
(Expressão Condicional)
"""

# logged_user = False
#
# if logged_user:
#     message = 'Usuário logado!'
# else:
#     message = 'Usuário não logado'
#
# print(message)
######## Sem expressão condicional ###########

###############################################################
# logged_user = False
#
# print('Usuario logado') if logged_user else print('Usuário não logado')
############ Usando a expressão condicional #############

idade = int(input('Qual a sua idade? '))

e_maior = (idade >= 18)

print('Idade válida para fazer o Cartão') if e_maior else print('Idade inválida para fazer o Cartão!')