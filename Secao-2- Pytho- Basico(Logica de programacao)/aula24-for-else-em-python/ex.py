"""
For / Else em Python
"""

lista = ['MARANATA', 'HORA', 'VEM', 'SENHOR', 'JESUS']

for item in lista:
    if item.startswith('J'):
        print('REI DOS REIS\nJesus')
    else:
        print(item)

print('#'*80)

del lista[-1]

for item in lista:
    print(item)
else:
    print('JESUS')

print('#'*80)

