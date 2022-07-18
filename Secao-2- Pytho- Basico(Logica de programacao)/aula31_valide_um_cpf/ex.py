cpf = '16899535009'
novo_cpf = cpf[0:9]
reverso = 10
total = 0

for indice in range(19):
    if indice > 8:
        indice -= 9

    total += int(novo_cpf[indice]) * reverso

    reverso -=1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

if cpf == novo_cpf:
    print('Válido')
else:
    print('Inválido')