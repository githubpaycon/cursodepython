nome = input('DIGITE SEU NOME: ')
idade = int(input('DIGITE SUA IDADE: '))
altura = float(input('DIGITE SUA ALTURA (COM PONTO): '))
peso = float(input('DIGITE SEU PESO: '))
e_maior = idade >= 18
imc = peso / (altura * altura)

# f strings
print(f'{nome} tem {idade} anos de idade, a sua altura é {altura} seu peso é {peso} e seu IMC é {imc:.2f} ')
