email_usuario = 'gablop6543@gmail.com'
pass_usuario = '123'

input_email = input('Qual o seu email? ')
input_senha = input('Qual a sua senha? ')

if input_email == email_usuario and input_senha == pass_usuario:
    print('Autorizado')
else:
    print('Não Autorizado, Por favor, tente novamente ;-)')
