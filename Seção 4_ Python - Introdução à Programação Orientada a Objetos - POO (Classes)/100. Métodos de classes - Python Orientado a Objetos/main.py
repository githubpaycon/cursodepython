import os
from random import randint

os.system('cls' if os.name == 'nt' else 'clear')  # se o sistema for nt é csl senao clear

class Pessoa():
    ano_atual = 2022  # atributo de classe
    
    
    # construtor
    def __init__(self, nome, idade):  # método relacionado à instância (self) 
        self.nome = nome
        self.idade = idade
    
    # método DE INSTÂNCIA
    def get_nascimento(self):  # método relacionado à instância (self)
        print(f'{self.nome} {self.ano_atual - self.idade}')
        
    @classmethod  # MÉTODO DE CLASSE
    def criar_pessoa_por_ano_de_nascimento(cls, nome, ano_nascimento):
        ''' método de classe, nao precisa estar disponível para outra
        instancia (self) mas apenas para a classe em si
            o método retorna a propria classe porem agora com nome e idade
            baseado nos parametros que mandamos
        '''
        
        idade = cls.ano_atual - ano_nascimento  # variavel disponivel só nesse escopo
        return cls(nome, idade) # executa a classe
    
    @staticmethod  # deixa o método abaixo como um metodo estático
    def gera_id():
        rand = randint(10000, 19999) # essa var só vai estar disponivel para a função gera_id
        return rand
        
        
pessoa = Pessoa('Gabriel', 20)  # tabém cria uma pessoa mas pela idade atual
pessoa.get_nascimento()
print(pessoa.gera_id())  # sendo executada com a instância
print(Pessoa.gera_id())  # sendo executada diretamente na classe
