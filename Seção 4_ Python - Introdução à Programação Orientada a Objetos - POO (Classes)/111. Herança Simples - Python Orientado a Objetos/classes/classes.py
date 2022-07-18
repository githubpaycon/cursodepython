# supondo que tenho um cadastro de clientes
class Cliente: # é Cliente e não clientes pois a classe é um molde para FAZER CLIENTES
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        # esse cliente também terá endereços mas o endereço será em uma a parte porque um cliente pode ter vários endereços
        self.enderecos = []  # nessa lista pretendo receber objetos da classe endereco
        
    def insere_endereco(self, cidade, estado):
        """Usamos a composição, que é utilizar uma outra classe para receber os objetos
            ou seja, utilizamos a classe endereço para compor/constituir/formar/produzir um cliente na classe
        """
        self.enderecos.append(Endereco(cidade=cidade, estado=estado))
        
    def __del__(self):
        print(f'{self.nome} Foi apagado')
        
    def lista_enderecos(self):
        print(f'O(A) cliente {self.nome} tem {len(self.enderecos)} endereços:')
        for endereco in self.enderecos:
            print(f'    Cidade: {endereco.cidade} & Estado: {endereco.estado}')
        else:
            print()
        
        
class Endereco: # cria objetos com a cidade e o estado
    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado
        
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO!')