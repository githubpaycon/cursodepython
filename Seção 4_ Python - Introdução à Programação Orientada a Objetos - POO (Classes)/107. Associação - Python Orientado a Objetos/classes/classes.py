class Escritor:
    def __init__(self, nome):
        self.__nome = nome  # atributo privado
        self.__ferramenta = None  # variável pronta para receber qualquer coisa
        import os
        os.system('clear')
    
    @property  # criando um getter
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta_do_escritor(self):
        return self.__ferramenta
    
    @ferramenta_do_escritor.setter  # cria um setter para setar o valor do atributo da instância __ferramenta que por padrão é None
    def ferramenta_do_escritor(self, sua_ferramenta):
        self.__ferramenta = sua_ferramenta
    
class Caneta:
    def __init__(self, marca, cor):
        self.__marca = marca
        self.__cor = cor
        
    # criando um getter para receber a marca da caneta
    @property
    def marca_da_caneta(self):
        return self.__marca
    
    @property
    def cor_caneta(self):
        return self.__cor
    
    def escrever(self):
        print(f'Caneta da marca {self.marca_da_caneta}, está escrevendo na cor {self.cor_caneta}')
    
class MaquinaDeEscrever:
    def escrever(self):
        print(f'Máquina da está escrevendo')