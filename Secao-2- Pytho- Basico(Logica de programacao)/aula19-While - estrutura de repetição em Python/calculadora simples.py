# calculadora simples

while True:  # while sempre será verdadeiro, usado para que o loop nunca tenha fim
    print()
    n1 = input('Digite um número: ')
    operador = (input('Digite um operador: '))  # + - / *
    n2 = input('Digite outro número: ')

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
