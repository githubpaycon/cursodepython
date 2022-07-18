import sys
from time import sleep
#
#
# def gera():
#     for item in range(10):
#         yield item
#         sleep(.5)
#
#
#
# g = gera()
#
# print(g)
# for v in g:
#     print(v)


lista = [n for n in range(1000)]
list_generator = (n for n in range(1000))
print(sys.getsizeof(lista))
print(sys.getsizeof(list_generator))

for num in list_generator:
    if num == 999:
        print(num, sys.getsizeof(list_generator))