"""
Formatando Valores Com Modificadores - Aula 5

:s - Texto (Strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)

:.nºf - Quantidade de casas decimais (usado em números float) EX: :.2f
:caractere (> ou < ou ^)(Quantidade)(tipo - s, d, ou f)

> - Esquerda
< - Direita
^ - Centro

falando que a nossa string/int/float pode ter um tamanho padrão
caso queira que a str/int/float tenha 10 casas e as casas que não foram preenchidads sejam preenchidas por 0 exemplo

Explicação da linha 6
: - É utilizado para mostrar ao interpretador do Python que vai ter uma formatação
.nºf - é utilizado para limitar o tamanho do número float em 2 casas decimais. ex 3.33 ao invés de 3.3333333333333335
"""

############################################################################


n1 = 10
n2 = 3
divisao = n1 / n2
print(f'a divisão fica {divisao}')
print(f'a divisão fica {divisao:.2f}')
print(f'a divisão fica {divisao:.0f}')  # sem número real / float

#######################################################################

nome = 'Gabriel Lopes'

print(f'{nome:s}')  # Simplesmente fala que é uma string
print(f'{nome:.2s}')  # aqui está sendo usado para limitar o tamanho da String

########################################################################

n1 = 11
print(f'{n1:0>10}')  # o numero 11 ficara à direita
print(f'{n1:0^10}')  # o numero 11 ficara no meio dos zeros
print(f'{n1:0<10}')  # o numero 11 ficará à esquerda do 11
print(f'{1111111:0<10}')  # Como são 10 casas decimais ficará 7 un's e três 0

###########################################################################

print(f'{n1:.2f}')  # para colocar casas decimais em números inteiros (n1 é um numero inteiro e foi colocado
# 2 casas decimais# )

print(f'{n1:0>10.2f}')  # aqui vai colocar 0 á esquerda do 11 e 2 casas de ponto flutuante

nome = 'Gabriel Lopes'
print(f'{nome:#^20}')  # para adicionar caracteres ao nome


nome2 = 'GAbriel lOpEs'
print(100 * '#')
print(nome2.capitalize())  # mostra a primeira letra em maiúscula e as outras minúsculas a partir do Python 3.8
print(nome2.islower())  # Pergunta para o interpretador se as letras são maiúsculas
print(nome2.lower())  # Deixa toda a string em minuscula
print(nome2.isupper())  # pergunta ao interpretador se a string é minúscula
print(nome2.upper())  # deixa a string toda em maiúscula
print(nome2.center(16, 'a'))  # deixa a string toda em maiúscula
print(nome2.title())  # deixa somente as primeiras letras em maiúscula

# vide documentação - https://www.tutorialspoint.com/python/python_strings.htm
