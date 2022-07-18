from classes.classes import (
    Escritor,
    Caneta,
    MaquinaDeEscrever
)


escritor = Escritor(nome='Gabriel')
caneta = Caneta(marca='Bic', cor='verde')
maquinadeescrever = MaquinaDeEscrever()

# criando a associação


escritor.ferramenta_do_escritor = caneta
escritor.ferramenta_do_escritor.escrever()

# quando deleta o escritor, ainda é possível usar caneta!
del escritor
caneta.escrever()

"""
A GENTE CRIOU UM escritor, UMA caneta, UMA maquinadeescrever 
E NA CLASSE ESCRITOR TEMOS O ATRIBUTO FERRAMENTA
DEPOIS FALAMOS QUE O GETTER FERRAMENTA_DO_ESCRITOR VAI RECEBER UM OBJETO INTEIRO A MÁQUINA OU A CANETA
O QUE SIGNIFICA QUE ESTAMOS MANDANDO UMA CLASSE INTEIRA (POR EXEMPLO A CLASSE MaquinaDeEscrever) PARA DENTRO DO
ATRIBUTO DA INSTÂNCIA __ferramenta
"""
