from dados import pessoas, produtos, lista

def idade_no_prox_ano(pessoa):
    pessoa['idade_no_prox_ano'] = pessoa['idade'] + 1
    return pessoa

pessoas_c_idades = map(idade_no_prox_ano, pessoas)
for pessoa in pessoas_c_idades:
    print(f'nome: {pessoa["nome"]},'
          f' idade: {pessoa["idade"]},'
          f' idade_ano+1: {pessoa["idade_no_prox_ano"]}')