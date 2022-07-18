def convert_num(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = convert_num(input('Digite um número: '))

    if numero is not None:
        print(numero * 5)
    else:
        print('Isso não é número!')

    # Mesma verificação mas invertida
    if numero == None:
        print('isso não é um numero')
    else:
        print(numero * 10)
