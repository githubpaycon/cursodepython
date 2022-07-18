nome = input('Qual o seu nome? ')

if 'Gabriel' in nome:
    print(f'Olá! mais um Gabriel por aqui!')
elif not 'Gabriel' in nome:
    print(f'Olá {nome}!')
else:
    pass  # O pass é usado quando eu ou outro programador não sabe o que vai escrever, como nesse exemplo
    ...  # isso é o mesmo que o pass usado para escrever posteriormente algo, como uma saida padrão.