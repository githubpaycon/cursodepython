import os
os.system('clear')

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        print('setter sendo executado')
        self._nome = f'Eu sou {nome}'
        return nome
    
    @property
    def sobrenome(self):
        return 'RUAN'

p1 = Pessoa(nome="otavio")
print(p1.nome, p1.sobrenome)