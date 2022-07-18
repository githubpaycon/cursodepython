import os
os.system('clear')
from classes.classes import (
    CarrinhoDeCompras,
    Produto
)

carrinho = CarrinhoDeCompras()

p1 = Produto(nome='Camiseta', valor=50)
p2 = Produto(nome='iPhone', valor=10000)
p3 = Produto(nome='Caneca', valor=15)

carrinho.inserir_produto(produto=p1)
carrinho.inserir_produto(produto=p2)
carrinho.inserir_produto(produto=p3)
carrinho.inserir_produto(produto=p1)

carrinho.lista_produtos()
print()
carrinho.soma_total()
