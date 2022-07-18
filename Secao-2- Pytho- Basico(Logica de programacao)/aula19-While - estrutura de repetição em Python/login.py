# Login de usuário usando while

# base de dados
bd_nome = 'Gabriel'
bd_usuario = 'gabriel'
bd_senha = '123321'
# base de dados

# verificação do usuário
usuario = ''
senha = ''
# verificação do usuário

while usuario != bd_usuario or senha != bd_senha:
    usuario = input('Digite o seu usuário: ')
    senha = input('Digite a sua senha: ')
    if usuario != bd_usuario or senha != bd_senha:
        print(f'Senha ou usuário inválidos, tente novamente.')
    if usuario == bd_usuario and senha == bd_senha:
        print(f'Bem vindo {bd_nome}')
