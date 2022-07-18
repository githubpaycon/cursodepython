class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []  # nessa lista pretendo receber objetos da classe Produto
        
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def lista_produtos(self):
        if self.produtos:
            print(f'Existe {len(self.produtos)} produto(s)')
            print()
            for produto in self.produtos:
                print(f'Nome produto: {produto.nome} | Valor produto: R$ {produto.valor}\n')
        else:
            print('Ainda não tem produtos')
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total = produto.valor + total
        return print(f'O total do carrinho é: R$ {total}\n')
            
class Produto:
    def __init__(self, nome, valor : int):
        self.nome = nome
        self.valor = valor
        