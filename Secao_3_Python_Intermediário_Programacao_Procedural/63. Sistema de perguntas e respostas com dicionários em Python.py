perguntas = {
    'pergunta1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {'a': '3', 'b': '4', 'c': '12'},
        'resposta_certa': 'b',
    },
    'pergunta2': {
        'pergunta': 'Qual a cor da laranja? ',
        'respostas': {'a': 'Azul', 'b': 'Verde', 'c': 'Laranja'},
        'resposta_certa': 'c',
    },
}

respostas_certas = 0

for perguntas_chave, pergunta in perguntas.items():  # pergunta chave é a pergunta1, e pergunta é todo o dicionário que tem dentro da pergunta contendo tambem as respostas e a resposta correta
    print(f'{perguntas_chave}: {pergunta["pergunta"]}')  # mostra pergunta(n) e a pergunta.

    print('Escolha uma das opções abaixo:')
    for resposta_letra, resposta in pergunta['respostas'].items():
        print(f'({resposta_letra}) {resposta}')
    else:
        resposta_usuario = input('Sua resposta: ')

        if resposta_usuario == pergunta['resposta_certa']:
            print('Parabéns acertou')
            respostas_certas += 1
        else:
            print('Errou!!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas. \nE a sua porcentagem de acerto foi: {porcentagem_acerto}')