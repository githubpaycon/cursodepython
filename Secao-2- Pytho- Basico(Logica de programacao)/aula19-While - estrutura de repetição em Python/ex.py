"""

while em Python
utilizado para realizar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores
"""

# while True:
#     nome = input('Qual o seu nome?')
#     print(f'Olá {nome}!')                loop infinito

x = 0

# exemplo continue #

# while x <= 5:
#     if x == 3:  # quando chegar aqui ele vai pular se for igual a 3
#         x = x + 1  # aqui será somado de 3 para 4 e o fluxo voltara até o 5
#         continue  # aqui ele não vai mostrar na tela o 3 porque vai pular o resto do código e vai voltar para a verificação
#     print(x)
#     x = x + 1

# exemplo break #

# while x <= 5:
#     if x == 3:  # quando chegar aqui ele vai pular se for igual a 3
#         x = x + 1  # aqui será somado de 3 para 4 e o fluxo voltara até o 5
#         break  # aqui ele vai sair totalmente do loop diferente do continue que apenas "retorna para o próprio loop"
#     print(x)
#     x = x + 1


# verificação de usuário usando while #

# # base de dados
# bd_nome = 'Gabriel'
# bd_usuario = 'gabriel'
# bd_senha = '123321'
# # base de dados
#
# # verificação do usuário
# usuario = ''
# senha = ''
# # verificação do usuário
#
# while usuario != bd_usuario or senha != bd_senha:
#     usuario = input('Digite o seu usuário: ')
#     senha = input('Digite a sua senha: ')
#     if usuario != bd_usuario or senha != bd_senha:
#         print(f'Senha ou usuário inválidos, tente novamente.')
#     if usuario == bd_usuario and senha == bd_senha:
#         print(f'Bem vindo {bd_nome}')


# Fazendo coordenadas
x = 0

# while x <= 10:
#     y = 0  # essa variável tem que estar dentro do primeiro while porque ele tem que voltar a ser 0 quando o while do y acabar
#     while y <= 10:
#         y += 1
#         print(f'({x}), ({y})')
#     x += 1

# calculadora simples

while True:  # while sempre será verdadeiro, usado para que o loop nunca tenha fim
    print()
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operador = (input('Digite um operador: '))  # + - / *

    # verificação de dados
    if n1.isdigit() and n2.isdigit():
        n1 = int(n1)
        n2 = int(n2)
    else:
        print('Inválido')
        continue
    # verificação de dados

    if operador == '+':
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
        sair = input('você quer sair da calculadora? S/N? ')
        if sair == 's' or sair == 'S':
            print('Obrigado por utilizar a nossa calculadora!')
            break
        else:
            continue
    elif operador == '-':
        print(f'A subtração entre {n1} e {n2} é {n1 - n2}')
        sair = input('você quer sair da calculadora? S/N? ')
        if sair == 's' or sair == 'S':
            print('Obrigado por utilizar a nossa calculadora!')
            break
        else:
            continue
    elif operador == '/':
        print(f'A divisão entre {n1} e {n2} é {n1 / n2}')
        sair = input('você quer sair da calculadora? S/N? ')
        if sair == 's' or sair == 'S':
            print('Obrigado por utilizar a nossa calculadora!')
            break
        else:
            continue
    elif operador == '*':
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
        sair = input('você quer sair da calculadora? S/N? ')
        if sair == 's' or sair == 'S':
            print('Obrigado por utilizar a nossa calculadora!')
            break
        else:
            continue
    else:
        print('Operador Inválido')
        sair = input('você quer sair da calculadora? S/N? ')
        if sair == 's' or sair == 'S':
            print('Obrigado por utilizar a nossa calculadora!')
            break
        else:
            continue
x %= 1
