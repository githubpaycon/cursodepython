nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
ano_nascimento = 2021 - idade
print(f'O usuário digitou {nome} e o seu tipo de dado é {type(nome)}')
print(f'O usuário digitou {idade} e o seu tipo de dado é {type(idade)}')
print(f'O usuário nasceu em {ano_nascimento}, e o tipo de dado é {type(ano_nascimento)}')
