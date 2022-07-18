"""
Crie uma função que receba 2 números. O primeiro é um valor
e o segundo um percentual (ex. 10%). Retorne (return) o
valor do primeiro número somado do aumento do percentual do mesmo.
"""


def aum_percent(v_item, v_aumento):
    fator_aumento = (v_aumento / 100) + 1
    v_final_conta = v_item * fator_aumento
    return print(v_final_conta)


aum_percent(50, 10)
aum_percent(100, 10)
aum_percent(10, 10)
aum_percent(15, 100)
