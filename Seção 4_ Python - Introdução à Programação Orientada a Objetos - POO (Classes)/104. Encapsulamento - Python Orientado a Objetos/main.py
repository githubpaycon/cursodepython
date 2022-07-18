import os
os.system('clear')

class BaseDeDados:
    def __init__(self) -> None:  # construtor
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados
    
    def inserir_cliente(self, id, nome):  # o id vai ser a chave e o nome, o valor
        if 'clientes' not in self.__dados: # se a chave clientes não existir no dict
            self.__dados['clientes'] = {id : nome}  # vai criar um dicionário de clientes
                                                  # e dentro desse dict vai ter 
                                                  # cada cliente com seu id e nome
        else:  # se cair aqui, significa que a chave cliente já existe no dict, ai é só atualizar o dict (ADD)
            self.__dados['clientes'].update({id : nome})
            
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():  # para cada id e nome no dicionario dados, 
                                                         # acesse clientes para pegar os dados
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]  # para o dicionario dados, 
                                        # acesse clientes e apague 
                                        # quem tem o id que foi enviado


db = BaseDeDados()
db.inserir_cliente(id=1, nome='Gabriel')
db.inserir_cliente(id=2, nome='João')
print(db.dados)