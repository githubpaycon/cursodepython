"""
Operadores Aritméticos

+ (Mais/adição)
- (Menos/subtração)
* (Multiplicação)
/ (Divisão)
// (divisão inteira 'O arredondamento da divisão')
** (Exponenciação/Potenciação)
% (Resto da divisão)
() (Prioridade no cálculo)
"""
# Básicos
print('Adição (+)', 10 + 10)
print('Subtração (-)', 10 - 10)
print('Multiplicação (*)', 10 * 10)
print('Divisão (/)', 10 / 2)

# Avançados
print('divisão inteira (//) ', 10.0 // 3)  # mostra a divisão inteira com ponto flutuante
print('divisão inteira (//) ', 10 // 3)  # mostra a divisão inteira sem ponto flutuante
print('divisão (/) ', 10 / 3)  # mostra a divisão com ponto flutuante GRANDE

print('Potenciação (**)', 2 ** 10)  # 2 elevado à 10 2^10
print('Resto da Divisão (%)', 10 % 3)  # só funciona com divisão que TEM resto
print('Ordem de Precedência (())', 5+2*10)  # Vai dar 25 pela ordem de precedência padrão
print('Ordem de Precedência (())', (5+2)*10)  # Vai dar 70 pela ordem de precedência dos parênteses

