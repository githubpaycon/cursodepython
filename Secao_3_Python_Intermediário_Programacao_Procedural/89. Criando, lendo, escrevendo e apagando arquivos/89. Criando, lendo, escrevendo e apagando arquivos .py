import json
with open('pessoas.json', 'r') as pessoas:
    pessoas_dict = json.load(pessoas)
for pessoa, dados in pessoas_dict.items():
    print(pessoa)
    for chave, dado in dados.items():
        print(f'    {chave}, {dado}')
