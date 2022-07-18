dici1 = {'nome': 'João', 'idade': '16', 'estado_civil': 'Solteiro', 'profissao': 'Corta Papel'}
clientes = {
    'client1': {
        'nome': 'Gabriel',
        'sobrenome': 'Lopes',
    },
    'client2': {
        'nome': 'João',
        'sobrenome': 'Souza',
    },
}

dici2 = {'salario': 11, 'estuda': True}


def deleta_chave(dicio, chave):  # exclui uma chave de um dicionário informando o dict e a key dele
    del dicio[chave]


def del_ultima_chave(dicio):
    dicio.popitem()


def tamn_dict(dici):  # vê o tamanho do dicionário
    return len(dici)


def ver_chaves(dicio):  # Mostra as chaves do dicionário
    for chave in dicio:
        print(chave)
    return ''


def ver_valores(dicio):  # mostra os valores de cada chave do dicionário
    for valor in dicio.values():
        print(valor)
    else:
        return ''


def ver_itens(dicio):  # mostra tanto as CHAVES quanto os VALORES (modo tuplas)
    for item in dicio.items():
        print(item)
    else:
        return ''


def ver_itens_not_tuple(dicio):  # mostra tanto as chaves quanto os valores
    for chave, valor in dicio.items():
        print(chave, valor)
    else:
        return ''


def itere_dicts(dicio):  # DEVE SER USADO SOMENTE COM DICIONARIOS QUE TEM DICIONARIOS FILHO
    for cliente_id, clientes_dados in dicio.items():
        print(f'Exibindo {cliente_id}')  # mostra o id do cliente
        for dado_nome, dado in clientes_dados.items():  # a cada loop mostra cada dado que o cliente tem
            print(f'\t{dado_nome} => {dado}')


def concatena_dicts(dict1, dict2):
    dict1.update(dict2)

concatena_dicts(dici1, dici2)

print(dici1)