print()

hora = input(f'Digite a HORA \nEx: 13: ')

if len(hora) <= 2 and hora.isnumeric():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa Noite!')
    elif hora < 0 or hora > 23:
        print('O horário tem que ser de 00 até 23')
else:
    print(f'O valor {hora} é inválido')
