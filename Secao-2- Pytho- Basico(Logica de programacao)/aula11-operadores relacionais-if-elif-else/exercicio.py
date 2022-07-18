# Recebe ou não o empréstimo
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

if idade >= 18 and idade <= 65:
    print(f'{nome}, seu empréstimo foi LIBERADO')
else:
    print(f'{nome}, seu empréstimo nâo FOI LIBERADO')
