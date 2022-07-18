"""
Operadores Lógicos - if - elif - else

and
or
not

in
not in
"""
# é necessario que as duas sejam verdadeiras para RETORNAR verdadeiro
# comparacao1 and comparacao2
# é necessario que as duas sejam verdadeiras para RETORNAR verdadeiro

# é necessario que pelo menos uma seja verdadeiro para dar verdadeiro
# comparacao1 or comparacao2
# é necessario que pelo menos uma seja verdadeiro para dar verdadeiro

# SEM INVERSÃO
if 2 > 1:
    print('2 é maior que 1')
else:
    print('2 é menor que 1')

# not é o de 'iversão'
if not 2 > 1:
    print('2 é maior que 1')
else:
    print('2 é menor que 1')
# not é o de 'iversão'

a = ''
b = 0
# o not é usado também para saber se a variável está vazia
if not a and not b:
    print('a variável NÂO tem valor')
else:
    print('a variável ESTÁ COM valor')
# pode ser utilizado quando o usuário não preenche algum dado.

nome = 'Gabriel'

if 'a' in nome:
    print('Existe "a" em seu nome')
else:
    print('Não existe "a" em seu nome')

# o not in simplesmente inverte o valor da expressão

nome = 'Gabriel'

if 'a' not in nome:
    print('Existe "a" em seu nome')
else:
    print('Não existe "a" em seu nome')

