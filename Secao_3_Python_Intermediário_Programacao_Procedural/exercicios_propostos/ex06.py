# def func1(salvador, criador):
#     salvador = salvador.upper()
#     criador = criador.upper()
#     print(salvador, criador)
#
#
# def func2():
#     salvador = 'é Jesus Cristo'
#     return salvador
#
#
# def func3():
#     criador = 'Deus'
#     return criador
#
#
# salvador = func2()
# criador = func3()
#
#
# func1(salvador, criador)
#
#



def mestre(funcao, *args, **kwags):
    return funcao()



def fala_oi(nome):
    return 'f Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'

executar = mestre(saudacao)

print(executar)