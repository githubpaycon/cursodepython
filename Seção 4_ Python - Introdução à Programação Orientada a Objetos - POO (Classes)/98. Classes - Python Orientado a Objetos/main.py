from pessoa import Pessoa  # do módulo pessoa, importe a classe Pessoa
import os

os.system('cls' if os.name == 'nt' else 'clear')


pessoa1 = Pessoa('Gabriel', 20)
pessoa2 = Pessoa('Jorge', 32)
pessoa3 = Pessoa('Carlos', 42)

pessoa1.comer('melancia')
pessoa2.falar(assunto='POO')
pessoa3.comer('Chocolate')

pessoa1.falar('POO')
pessoa1.parar_comer()
pessoa1.falar('POO')

pessoa3.parar_comer()
pessoa2.parar_falar()

pessoa1.get_ano_nascimento()
pessoa2.get_ano_nascimento()
pessoa3.get_ano_nascimento()