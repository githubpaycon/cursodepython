'''
Combinations, Permutations, Product - Itertools
Combinação - ORDEM NÃO IMPORTA
Permutação - ORDEM IMPORTA
AMBOS NÃO REPETEM VALORES ÚNICOS
Produto = ORDEM IMPORTA E REPETE VALORES ÚNICOS
'''
from itertools import product
pessoas = ['Jesus', 'André', 'Gabriel', 'João', 'Reinaldo', 'Emilia']


for dupla in product(pessoas, repeat=2):
    print(dupla)