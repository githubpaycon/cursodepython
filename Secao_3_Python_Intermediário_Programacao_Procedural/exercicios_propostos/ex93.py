"""
Faça uma lista de tarefas com as seguintes opções:
adicionar tarefa
listar tarefas
opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
opção de refazer (a cada vez que chamarmos, refaz a última ação)
['Tarefa 1', 'Tarefa 2']
['Tarefa 1'] <- Desfazer
['Tarefa 1', 'Tarefa 2'] <- Refazer
input <- Nova tarefa
"""


def mostra_tarefas(lista_de_tarefas):
    if lista_de_tarefas:  # se existir algo na lista de tarefas...
        print()
        print('Tarefas: ')
        for i in lista_de_tarefas: # mostra cada item da lista
            print(f'* {i}')
        print()
    else:  # senão...
        print('Ainda não existe tarefas...')
        


def fazer_desfazer(lista_de_tarefas, lista_de_refazer):
    if not lista_de_tarefas:
        print('Nada a desfazer')
        return

    ultima_tarefa = lista_de_tarefas.pop()  # remove da lista de tarefas
    lista_de_refazer.append(ultima_tarefa)  # adiciona para a lista de desfazer


def fazer_refazer(lista_de_tarefas, lista_de_refazer):
    if not lista_de_refazer:
        print('Nada a refazer')
        return

    ultimo_refazer = lista_de_refazer.pop()
    lista_de_tarefas.append(ultimo_refazer)


def adicionar_tarefa(tarefa, lista_de_tarefas):
    lista_de_tarefas.append(tarefa)
    print('\n\nTarefa adicionada com sucesso!\n\n')


if __name__ == '__main__':
    lista_de_tarefas = []
    lista_de_refazer = []

    while True:
        faca = input('O que você deseja fazer?\n'
                     '1 - Adicionar tarefa\n'
                     '2 - Desfazer...\n'
                     '3 - Refazer...\n'
                     '4 - Listar Tarefas... \n\n'
                     '>>> ')

        if faca == '4':
            mostra_tarefas(lista_de_tarefas)
            continue
        elif faca == '2':
            fazer_desfazer(lista_de_tarefas, lista_de_refazer)
            continue
        elif faca == '3':
            fazer_refazer(lista_de_tarefas, lista_de_refazer)
            continue
        elif faca == '1':
            tarefa = input('Escreva sua tarefa: ')
            adicionar_tarefa(tarefa, lista_de_tarefas)
            continue
        else:
            print('Você digitou algo errado...')
            continue