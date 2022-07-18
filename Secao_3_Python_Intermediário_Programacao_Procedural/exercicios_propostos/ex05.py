# Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada#

def funcao1():
    valor = 'Jesus é o Salvador'
    return valor


def funcao2(arg):
    arg = arg.upper()  # para manipular uma variável tem que atribui-lá em um parâmetro
    print(arg)


var_func1 = funcao1()

funcao2(var_func1)
