"""
Fizz Buzz Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz.
Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz,
caso contrário, retorne o número enviado."""
import random


def fizzbuzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return print(f'FizzBuzz ({n})')
    elif n % 3 == 0:
        return print(f'Fizz ({n})')
    elif n % 5 == 0:
        return print(f'Buzz ({n})')
    else:
        return print(n)


fizzbuzz(random.randint(1, 999))
fizzbuzz(15)