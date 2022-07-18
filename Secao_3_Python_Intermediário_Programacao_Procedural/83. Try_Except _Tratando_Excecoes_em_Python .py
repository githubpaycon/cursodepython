# # '''
# # TRATAR UM ERRO INESPERADO
# # '''
# # int(input('Digite um número: '))
# #
# # try:
# #     int(input('Digite um número: '))
# #     # EXPLICAÇÃO
# #     '''
# #     VAI TENTAR EXECUTAR
# #     ESSE BLOCO, CASO O USER
# #     DIGITE UMA LETRA,
# #     CAIRÁ NO except
# #     '''
# # except NameError as desc_except:
# #     # EXPLICAÇÃO
# #     '''
# #     CAINDO NO except, A EXCEÇÃO SERÁ
# #     DO TIPO (NameError) E SERÁ ADD Á
# #     UMA VARIÁVEL, APELIDADA COMO
# #     desc_except, QUE É A DESCRIÇÃO DO
# #     ERRO.
# #     '''
# #     print(f'Erro do desenvolvedor...\n'
# #           f'Erro occorrido: {desc_except}')
# # except Exception as descrip_except:
# #     # EXPLICAÇÃO
# #     '''
# #     CASO OCORRA UM ERRO QUE NÁO É DO
# #     TIPO NameError, CAIRÁ NESSE except
# #     QUE ATRIBUI A DESCRIÇÃO DO ERRO NA
# #     VARIÁVEL descrip_except:
# #     '''
# #     print(f'Erro inesperado!\n'
# #           f'Mostre para o DEV: \n'
# #           f'{descrip_except}')
# #
# # print()
# # print('O programa não parou!')
#
#
#
#
# # Tratar 2 exeções no mesmo except #
# try:
#     lista = []
#     dicio = {}
#
#     print(dicio['Chave'])
# except NameError as descricao_erro:
#     print('Erro do dev\n'
#           f'Erro: {descricao_erro}')
# except (IndexError, KeyError) as descricao_erro:
#     # Aqui trata 2 exceções #
#     print('Erro de indice ou de chave não encontrada\n'
#           f'Erro: {descricao_erro}')
# except SyntaxError as descricao_erro:
#     print('Ocorreu um erro de syntaxe '
#           'o DEV não estava esperando...')
# except Exception as descricao_erro:
#     print('Ocorreu um erro que '
#           'o DEV não estava esperando...\n'
#           f'Erro: {descricao_erro}')
# else:
#     print('Não houve erros')



# Else no try except #

try:
    pessoas = [  # Lista de dict´s
        {},
        {'nome': 'Gabriel', 'idade': 19},
        {'nome': 'Joel', 'idade': 41},
        {'nome': 'Vitor', 'idade': 12},
    ]
except KeyError:
    print('A chave citada não existe')
except Exception:
    print('Erro Crítico')
else:
    print('Código, funcionou')
finally:
    print('Fechando arquivo contendo os nomes...')
    pessoas = []

for pessoa in pessoas:
   print(pessoa['nome'])