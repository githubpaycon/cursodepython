from dados import produtos, pessoas, lista
from functools import reduce

# soma total dos produtos

soma_precos_prod = reduce(lambda total, produto:
               produto['preco'] + total, produtos, 0)

# explication
'''
Na variavel soma_precos_prod, na função reduce()
a função reduce() recebe um lambda
esse lambda tem uma variável total
e uma variavel produto 
(produto que vem do carrinho exemp)
o preco do produto (produto['preco'])
será somado com o total, que inicia
com 0.
Isso tudo vem do dicionario produtos
'''

# pegar media dos precos dos produtos

total_precos = reduce(lambda total, produto:
                      produto['preco'] + total, produtos, 0)
media_precos = total_precos / len(produtos)



# explication
'''
Na variavel total_precos, na função reduce()
a função reduce() recebe um lambda
esse lambda tem uma variável primaria
como total e uma variavel segundária 
como produto (produto que vem do carrinho)
o preco do produto (produto['preco'])
será somado com o total, que inicia
com 0. isso ocorre até acabar os produtos
do carrinho.

PARA FAZER A MÉDIA

Pegou o resultado da variável total_precos e
dividiu pela quantidade de produtos.
pois para ver a média, tem que somar
todos os valores dos produtos e dividir
pela quantidade de produtos.
'''

# SOMAR AS IDADES

somar_idades = reduce(lambda total, pessoa:
                      pessoa['idade'] + total, pessoas, 0)
print(somar_idades / len(pessoas))

