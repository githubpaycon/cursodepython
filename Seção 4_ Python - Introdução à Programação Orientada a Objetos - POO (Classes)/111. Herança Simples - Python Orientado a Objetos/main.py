from classes.classes import Cliente


cliente1 = Cliente('gabriel', 20)
cliente1.insere_endereco('São Paulo', 'SP')
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 23)
cliente2.insere_endereco('Belo Horizonte', 'MG')
cliente2.insere_endereco('Salvador', 'BA')
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('Teresina', 'PI')
cliente3.insere_endereco('Salvador', 'BA')
cliente3.insere_endereco('Salvador', 'BA')
cliente3.lista_enderecos()
del cliente3
print()

print('########### fim do codigo ##############')
