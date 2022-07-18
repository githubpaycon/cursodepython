frase = 'O rato roeu a roupa do senhor'
tamanho_frase = len(frase)
contador = 0
nova_frase = ''

while contador < tamanho_frase:  # o tamanho_frase sempre vale 29
    letra = frase[contador]  # a letra é o número do contador do while se pegar 2 está pegando o r
    if letra == 'r':
        nova_frase += letra.upper()
    else:
        nova_frase += letra
    contador += 1
else:
    print(nova_frase)
