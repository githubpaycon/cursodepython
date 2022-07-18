"""
Tipos primitivos

str -> string -> 'Olá', ''Olá'', '''Olá'''(O mais recomendável para textos que tem aspas simples/duplas), "Olá", ""Olá""
int -> Números inteiros -> 1, 12, 3123, (Zero) 0, -1, -12, -3123
float -> Números de ponto flutuante/real -> 1.341, 10.423, 0.0, 0.2453, -7.532
bool -> boolean/lógico -> True/False ex: 10 == 10
"""

print('isso é uma str (string)', type('isso é uma str (string)'))       # string type
print(10, type(10))                                                     # int type
print(0.0, type(0.0))                                                   # float type

# (estou perguntando ao interpretador se 10 é igual a 10, e não declarando)
print(10 == 10, type(10 == 10))                                         # boolean type
# (estou perguntando ao interpretador se 10 é igual a 10, e não declarando)

# Conversão de tipos
print(10, type(10), float(10))  # De int para float
print(10.4124, type(10.4124), int(10.4124))  # De float para int
print(1, type(1), bool(1))  # De int para boolean/logic
print(10 == 10, type(10 == 10), int(10 == 10))  # de boolean para int (caso o resultado de 1 == true, 0 == false)
print(10 == 11, type(10 == 11), int(10 == 11))  # de boolean para int (caso o resultado de 1 == true, 0 == false)
print(True, type(True), int(True))  # de boolean para int (caso o resultado de 1 == true, 0 == false)
print(False, type(False), int(False))  # de boolean para int (caso o resultado de 1 == true, 0 == false)
