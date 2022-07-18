from itertools import groupby

alunos_lista = [
    {'nome': 'Gabriel', 'nota': 'A'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Reinaldo', 'nota': 'A'},
    {'nome': 'Emilia', 'nota': 'C'},
    {'nome': 'José', 'nota': 'D'},
    {'nome': 'Ricardo', 'nota': 'A'},
    {'nome': 'Mauricio', 'nota': 'B'},
    {'nome': 'Jesus', 'nota': 'A'},
    {'nome': 'Davi', 'nota': 'C'},
    {'nome': 'Israel', 'nota': 'B'},
]

ordene = lambda aluno: aluno['nota']

alunos_lista.sort(key=ordene)

alunos_agrupados = groupby(alunos_lista, ordene)
for grupo, alunos_notas in alunos_agrupados:
    print(f'\nAlunos que tiraram: {grupo}')
    quantidade = len(list(alunos_notas))
    print(f'    {quantidade} alunos tiraram a nota {grupo}')

