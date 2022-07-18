from math import pi as PI

def dobra_val_in_lists(lista):
    return [num * 2 for num in lista]

def multiplica(lista):
    total = 1
    for num in lista:
        total = num * total
      # total *= num
    return total

lista = [1,2,3,4,5]

if __name__ == '__main__':
    print(f'Os valores multiplicados: \n'
          f'{dobra_val_in_lists(lista)}\n\n'
          f'Valores multiplicados e somados:\n'
          f'{multiplica(lista)}\n\n'
          f'Valor de Pi: \n'
          f'{PI}')

    print(__name__)