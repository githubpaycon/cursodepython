nome = input('Qual o seu nome? ')

tamanho = len(nome)  # (len é o tamanho da string) sempre que perceber que tem que usar
# muito uma função use uma variável como esta

if tamanho == 0:
    print('Você não digitou nada!')
elif nome.isnumeric():
    print('Seu nome não pode ser um número!')
elif tamanho <= 4:
    print('Seu nome é Pequeno')
elif tamanho >= 5 and tamanho <= 6:
    print('Seu nome é Normal')
elif tamanho > 6:
    print('Seu nome é Grande!')
else:
    print('ERROR')