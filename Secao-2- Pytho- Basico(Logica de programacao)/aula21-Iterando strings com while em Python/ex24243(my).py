#
#        0123456789........................
frase = input('Escreva uma frase: ')
tamanho_da_frase = len(frase)
contador = 0
nova_str = ''

print(f'A frase é essa: {frase}')
print()
letra_escolhida = input('Qual letra deseja colocar em maiúscula: ')

while True:
    while contador < tamanho_da_frase:
        letra = frase[contador]
        if letra_escolhida.isupper() or letra_escolhida.isnumeric() or len(letra_escolhida) > 1:
            print('Erro. Tente novemente!')
            letra_escolhida = input('Qual letra deseja colocar em maiúscula: ')
        if letra == letra_escolhida:
            nova_str = nova_str + letra_escolhida.upper()  # concatenação
        else:
            nova_str = nova_str + letra  # concatenação
        contador += 1

    print(nova_str)
    retornar = input('Você quer jogar denovo?(S/N) ')
    if retornar == 'sim' or retornar == 'Sim' or retornar == 'SIM' or retornar == 'S' or retornar == 's':
        contador = 0
        nova_str = ''
        letra_escolhida = input('Qual letra deseja colocar em maiúscula: ')
        continue
    else:
        break
