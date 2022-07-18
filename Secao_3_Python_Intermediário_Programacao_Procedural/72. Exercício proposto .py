carrinho = []

carrinho.append(['Produto1', 30])
carrinho.append(['Produto2', 20])
carrinho.append(['Produto3', 50])
carrinho.append(['Produto4', 50])
carrinho.append(['Produto4', 31.11])
carrinho.append(['Produto4', 1])

total = sum([float(preco) for produto, preco in carrinho])
# converte a lista total em uma soma com a função sum(), converte o preço para valor de ponto flutuante, e para cada for, pega o produto
#e o preço do carrinho, mas só será necessário pegar o preço

print(total)









# carrinho = dict(carrinho)
#
# itens = [preco for produto, preco in carrinho.items()]
#
# soma = 0
# lista_preco = [soma + preco for preco in itens]
# print()
# print(lista_preco)
# print()
# for preco in itens:
#     soma += preco
# print(soma)