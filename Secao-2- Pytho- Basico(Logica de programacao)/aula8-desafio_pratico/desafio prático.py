# vars
nome = input('Qual o seu nome? ')
ano_nascimento = int(input(f'Qual o seu ANO de nascimento {nome}? '))
altura = float(input(f'Qual a sua altura? '))
peso = float(input(f'E o seu peso? '))
ano_atual = 2021

# calc's
idade = ano_atual - ano_nascimento
imc = peso / altura ** 2

print(f'Prontinho {nome}!\n')
print(f'Pelo o que ví, você tem {idade} anos e nasceu no ano {ano_nascimento}!'
      f' e além disso, com a sua altura que é {altura} e seu peso que é {peso}'
      f' consegui o seu IMC,\n que é {imc:.2f}. Fica com Deus!')
