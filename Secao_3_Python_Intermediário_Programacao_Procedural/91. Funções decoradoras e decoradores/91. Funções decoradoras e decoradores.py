'''
a funcao velocidade recebe outra funcao como parametro
a funcao velocidade tem uma função chamada intera que
recebe argumentos não nomeados e argumentos nomeados (nao sei a qtd de argumentos)
e a funcao interna vai retornar e executar a funcao que vem do parametro da funcao velocidade
e a funcao velocidade vai retornar a interna sem executar

def velocidade(funcao):
    def interna(*args, **kwargs):
        funcao(*args, **kwargs)
    return interna
'''
from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()  # pega o tempo atual
        resultado = funcao(*args, **kwargs)  # executa a função
        end_time = time()  # pega o tempo atual (depois de ter executado a funçao)
        tempo_exec = (end_time - start_time) * 1000
        # para pegar os milesegundos pega o tempo depois de exectar a funcao e subtrai pelo tempo que foi iniciada
        # depois multiplica por mil (1000)
        print(f'\nA função "{funcao.__name__}" levou {tempo_exec:.2f}ms para executar')
        return resultado
    return interna


'''
Vai executar procurando() como paramentro para velocidade
'''
@velocidade
def procurando():
    for i in range(16):
        print(i, end='')

procurando()