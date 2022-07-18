"""
Variáveis


"""
nome = input('DIGITE SEU NOME: ')
idade = int(input('DIGITE SUA IDADE: '))
altura = float(input('DIGITE SUA ALTURA (COM PONTO): '))
peso = float(input('DIGITE SEU PESO (COM PONTO): '))
e_maior = idade >= 18
imc = peso / (altura * altura)

print(nome, 'tem', idade, 'anos de idade a sua altura é de', altura, 'e peso', peso, 'e é maior de idade?', e_maior, 'e seu IMC é:', imc)
