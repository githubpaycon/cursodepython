from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    # variável da classe, global para todos os métodos e instâncias (self's)
    
    # a método __init__ cria o self (cria a pessoa)
    def __init__(self, nome, idade, comendo=False, falando=False): 
        # o self é a pessoa
        self.nome = nome  # o self vai ter o nome que vir do parametro
        self.idade = idade  # a idade do self,
        self.comendo = comendo  # o self vai estar comendo?
        self.falando = falando  # # o self vai estar falando?
        
    def falar(self, assunto):  # metodo falar que recebe a pessoa e o assunto
        if self.comendo:  # se a pessoa estiver comendo
            print(f'{self.nome} não pode falar sobre {assunto} pois está comendo.')
            return

        if self.falando:  # se estiver falando (falando = true)
            print(f'{self.nome} já está falando, e o assunto é sobre {assunto}.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')  # caso nem esteja falando nem comendo
        self.falando = True  # define que a pessoa está falando

    def parar_falar(self):  # metodo para parar de falar
        if not self.falando:  # se a pessoa NAO estiver falando
            print(f'{self.nome} não está falando')  
            return

        print(f'{self.nome} parou de falar.')  # se a pessoa Estiver falando será definido para parar
        self.falando = False  # define que a pessoa parou de falar

    def comer(self, alimento):  # metodo para comer
        if self.comendo:  # ser apessoa já estiver comendo
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:  # se a pessoa estiver falando
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')  # se a pessoa nao está falando nem comendo
        self.comendo = True  # define que a pessoa está comendo

    def parar_comer(self):  # método para parar de comer
        if not self.comendo:  # se a pessoa não estiver comendo, 
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')  # caso a pessoa queira parar de comer
        self.comendo = False  # define que a pessoa parou de comer
        
    def get_ano_nascimento(self):
        return print(f'{self.nome} nasceu em {self.ano_atual - self.idade}')