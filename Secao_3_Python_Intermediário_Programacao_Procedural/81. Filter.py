from dados import produtos, pessoas, lista


def filtra(produto):
    if produto['preco'] > 50:
        return True


nova_lista = filter(filtra, produtos)
for t in nova_lista:
    print(t)

for x, y in enumerate(nova_lista):
    print(f'Tô imprimindo x {x}')
    print(f'Tô imprimindo y {y}')
    for w, z in y.items():
        print(f'Tô imprimindo w {w}')
        print(f'Tô imprimindo z {z}')