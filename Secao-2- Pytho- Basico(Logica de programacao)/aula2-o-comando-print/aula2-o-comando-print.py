print(1234567)

# O QUE TEM ENTRE OS PARENTESES SÃO ARGUMENTOS

'''NA FUNÇÃO PRINT, QUANDO UMA VIRGULA É ADICIONADA ENTRE DOIS ARGUMENTOS, DA O ESPAÇO AUTOMATICAMENTE'''

print('1ºargumento', '2ºargumento', '3ºargumento')
print(1, 2, 3)

'''
PARA USAR OUTRA COISA ENTRE OS ARGUMENTOS QUANDO COLOCAR A VIRGULA QUE NÃO SEJA ESPAÇO DEVE-SE ADICIONA NO FINAL DA FUNÇÃO sep='CARACTERE QUE QUER NA SEPARAÇÃO'
'''
# EX

print('Gabriel', 'Lopes', 'Souza', sep='-',)

'''
O END='' É USADO PARA NÃO PULAR AS LINHAS NO PRINT E NÃO ADICIONAR NENHUM ESPAÇO
'''
print('Gabriel', 'Lopes', 'Souza', sep='-', end='')
print('Gabriel', 'Lopes', 'Souza', sep='-', end='#####')
print('Gabriel', 'Lopes', 'Souza', sep='-', end='')
