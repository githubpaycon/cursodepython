# no 91. Funções decoradoras e decoradores.py
from vendas.calc_precos import aumento, reducao
# do pacote vendas, no modulo calc_precos, importe funcoes (pode ser variaveis) aumento e reducao
from vendas.formata.preco import formata_p_real

racao_8kg = 49.90
aumento_de_preco = aumento(racao_8kg, 15)
queda_de_preco = reducao(racao_8kg, 15)

if __name__ == '__main__':

      print(f'Houve um aumento de 15% na ração:\n'
            f'preço antes: {formata_p_real(racao_8kg)}\n'
            f'preco agora: {formata_p_real(aumento_de_preco)}\n\n')

      print(f'Houve uma queda de 15% na ração:\n'
            f'preço antes: {formata_p_real(racao_8kg)}\n'
            f'preco agora: {formata_p_real(queda_de_preco)}')
