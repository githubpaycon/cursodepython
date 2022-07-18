import os
os.system('cls' if os.name == 'nt' else 'clear')  # se o sistema for nt é csl senao clear

class Pessoa():
    ano_atual = 2022  # atributo de classe
    
    
    # construtor
    def __init__(self, nome, idade):  # método relacionado à instância (self) 
        self.nome = nome
        self.idade = idade
    
    # método
    def get_nascimento(self):  # método relacionado à instância (self)
        print(f'{self.nome} {self.ano_atual - self.idade}')
        
    @classmethod
    def criar_pessoa_por_ano_de_nascimento(cls, nome, ano_nascimento):
        ''' método de classe, nao precisa estar disponível para outra
        instancia (self) mas apenas para a classe em si
            o método retorna a propria classe porem agora com nome e idade
            baseado nos parametros que mandamos
        '''
        
        idade = cls.ano_atual - ano_nascimento  # variavel disponivel só nesse escopo
        return cls(nome, idade) # executa a classe  
        
        
pessoa1 = Pessoa.criar_pessoa_por_ano_de_nascimento('Gabriel', 2002)  # cria a pessoa pela data da nascimento
pessoa2 = Pessoa('Jorge', 20)  # tabém cria uma pessoa mas pela idade atual

print(pessoa1, 'pessoa1')
print(pessoa1.nome, pessoa1.idade)
pessoa1.get_nascimento()
"""
a unica diferença de um para o outro é que o pessoa1 cria a pessoa_pelo_ano_de_nascimento, usa um método da classe
    que faz um calculo para saber a idade do individuo, pega o ano atual e subtrai pela data de nascimento
    e no final retorna o nome e a idade para ser adicionado no self pelo __init__ para criar o objeto (instância)
    
    no pessoa2 o objeto já é criado diretamente pelo __init__ e não é passado para o método da classe
"""
print()
print(pessoa2, 'pessoa2')
print(pessoa2.nome, pessoa2.idade)
pessoa2.get_nascimento()