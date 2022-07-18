from mailbox import NotEmptyError
from wsgiref.validate import validator


class Produto:
    def __init__(self, nome_produto, preco_produto):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        
    def desconto(self, percentual):
        """caso a loja esteja em promoção
        utilize p/ exemplo 15% de desconto"""

        # o preco do produto recebe o percentual / 100 
        # esse calculo é multiplicado pelo preço do produto 
        # que no final é subtraido pelo preço do produto
        self.preco_produto = self.preco_produto - (self.preco_produto * (percentual / 100))

    @property
    def nome_produto(self):
        return self._nome_produto
    
    @nome_produto.setter
    def nome_produto(self, nome):
        nome = nome.capitalize()
        self._nome_produto = nome
        

    # GETTER # SEMPRE QUE PEDIR ESSE VALOR ESSE MÉTODO VAI SER CHAMADO ANTES DE PASSAR PELO __init__ 
    @property # -> decorador / propriedade
    def preco_produto(self):# esse método tem que ter o mesmo nome do parâmetro que seria criado pelo __init__
        # return self.preco_produto  
        # por convenção não se pode usar o nome do parâmetro do __init__ pois pode dar um loop muito doido
        # para resolver isso coloque um anderline "_"
        return self._preco_produto 
        
    @preco_produto.setter
    def preco_produto(self, valor):  # O VALOR É O QUE SERÁ ATRIBUIDO NO __init__
        if isinstance(valor, str):  # validando se é str (verifica se o valor da instância da classe str)
            valor = float(valor.replace('R$', ''))
            # se é uma string, o valor vira um float e é removido o "R$" do valor
        self._preco_produto = valor # tem que ser o mesmo valor definido pelo getter
    
    
camiseta = Produto('CAMISETA', 50)
camiseta.desconto(10)
print(camiseta.nome_produto, camiseta.preco_produto)

caneca = Produto('CANECA', 'R$15')
caneca.desconto(10)
print(caneca.nome_produto, caneca.preco_produto)
