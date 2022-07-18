from itertools import zip_longest

produtos = ['Arroz', 'Feijão', 'Macarrão', 'Molho de Tomate']  # tem 4 itens
preco_prod = [14.59, 7.90, 1.47]  # tem 3 precos
qtd_prod = [2, 4, 3]  # tem 3 valores de qtd's

carrinho = zip_longest(produtos, preco_prod, qtd_prod, fillvalue='Não Tem')

for prod, prec, qtd in carrinho:
    print(f'Produto: {prod}. Preço: {prec}. Quantidade: {qtd}')

# Saida >>>
# Produto: Arroz. Preço: 14.59. Quantidade: 2
# Produto: Feijão. Preço: 7.9. Quantidade: 4
# Produto: Macarrão. Preço: 1.47. Quantidade: 3
# Produto: Molho de Tomate. Preço: Não Tem. Quantidade: Não Tem