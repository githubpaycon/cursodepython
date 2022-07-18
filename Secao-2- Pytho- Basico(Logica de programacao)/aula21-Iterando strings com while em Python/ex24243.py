#               indice
#        0123456789........................
frase = 'o rato roeu a roupa do rei de roma'
tamanho_da_frase = len(frase)
contador = 0
nova_str = ''

print(f'A frase é essa: {frase}')
print()
letra_escolhida = input('Qual letra deseja colocar maiúscula? ')

while contador < tamanho_da_frase:
    letra = frase[contador]
    if letra == letra_escolhida:
        nova_str = nova_str + letra_escolhida.upper()  # concatenação
    else:
        nova_str = nova_str + letra  # concatenação
    contador += 1

print(nova_str)
