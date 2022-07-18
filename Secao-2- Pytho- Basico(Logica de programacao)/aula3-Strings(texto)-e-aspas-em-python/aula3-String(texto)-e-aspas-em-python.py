# str = string
# string é um texto dentro de aspas

print('Essa é uma string (str)')
print('''Essa é uma string (str)''')
print("Essa é uma string (str)")
print("""Essa é uma string (str)""")

# (aqui da erro no interpretador) print('Essa é uma 'string' (str)')
print('''Essa é uma 'string' (str)''')
print("Essa é uma 'string' (str)")
print("""Essa é uma 'string' (str)""")

# Pode ser usado também o caractere de escape \'
print('Essa é uma \'string\' (str)')

# \n é para quebrar linha
# o r atras da aspas mostra para o interpretador não ler nada que está dentro das aspas.

print(r'Essa é uma string \n (str)')

print('luiz', int('luiz'))