"""
109. Composição - Python Orientado a Objetos
composição é a relação mais forte entre classes

Uma classe vai ser dona de objetos de outra classe

@ caso a classe principal seja apagada, todos os objetos que a classe principal utilizou, também serão apagados


# EVITAR AO MÁXIMO DIGITAR MUITO CÓDIGO NO MAIN

# supondo que tenho um cadastro de clientes
class Cliente: # é Cliente e não clientes pois a classe é um molde para FAZER CLIENTES
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        # esse cliente também terá endereços mas o endereço será em uma a parte porque um cliente pode ter vários endereços
        self.enderecos = []  # nessa lista pretendo receber objetos da classe endereco
        
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade=cidade, estado=estado))
        
    def lista_enderecos(self):
        print(f'O(A) cliente {self.nome} tem {len(self.enderecos)} endereços:')
        for endereco in self.enderecos:
            print(f'    Cidade: {endereco.cidade} & Estado: {endereco.estado}')
        else:
            print()
        
        
class Endereco: # cria objetos com a cidade e o estado
    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado
        
        
#########################
Ao finalizar a execução de todo o código, mostrará o que foi apagado
########### fim do codigo ##############  # o garbage collector apagou tudo abaixo
gabriel Foi apagado
São Paulo/SP FOI APAGADO!
João Foi apagado
Salvador/BA FOI APAGADO!
Salvador/BA FOI APAGADO!
Teresina/PI FOI APAGADO!

Mostrando quando uma classe vai se apagada da memoria 
 NO MOMENTO EM QUE UM ELEMENTO É APAGADO DA MEMÓRIA, TODOS OS ENDEREÇOS SÃO DELETADOS COM ELE
 POR ISSO QUE AO APAGAR GABRIEL DELETA-SE LOGO DEPOIS O ENDEREÇO
 
gabriel Foi apagado  APAGOU O CLIENTE E TODOS OS ENDEREÇOS FORAM APAGADOS
São Paulo/SP FOI APAGADO!

Maria Foi apagado  APAGOU O CLIENTE E TODOS OS ENDEREÇOS FORAM APAGADOS
Salvador/BA FOI APAGADO!
Belo Horizonte/MG FOI APAGADO!

João Foi apagado  APAGOU O CLIENTE E TODOS OS ENDEREÇOS FORAM APAGADOS
Salvador/BA FOI APAGADO!
Salvador/BA FOI APAGADO!
Teresina/PI FOI APAGADO!



###################
Eu acho que entendi, o que quis dizer (me corrija se achar que eu não entendi rsrs)

Então... Você rapidamente vai aprender que quanto mais a gente separar as coisas, mais coeso fica o nosso software. Por exemplo, se eu adiciono tudo na classe do "Cliente" (só uma suposição), só teria desvantagem no meu programa... Toda vez que eu precisar mexer no endereço, eu vou estar mexendo no cliente (e vice versa). Se eu já escrevi testes para a classe do Cliente (ou Endereço), toda vez que eu alterar essa classe, eu vou precisar retestar ou talvez reescrever novos testes para a outra... Se eu escrever uma linha de código incorreta, eu vou derrubar duas coisas ao mesmo tempo, Cliente e Endereço... E por aí vai... Tudo o que você fizer em uma classe que "faz mais de uma coisa", é efeito em dose dupla (ou quantas coisas você misturar numa classe).

Na programação existe um princípio (dentre vários outros) chamado de "Princípio da responsabilidade única"... Em um super resumo, esse princípio diz que uma classe deve ter apenas um motivo para mudar... Por motivo, entenda como o elemento principal da classe... Por exemplo, "Endereço" e "Cliente" são duas coisas, certo? Nesse caso, o princípio indica que "Endereço" é uma classe, "Cliente" outra...

Em alguns casos, poderíamos dividir muito mais ainda... Exemplo, talvez "nome" e "sobrenome" do cliente, poderiam ser uma classe específica sobre isso, id poderia ser outra classe, talvez "rua", possa ter uma classe específica dependendo da complexidade dos nomes de ruas do país...

Por isso temos a composição (por composição, entenda agregação, associação ou composição)... Nós poderíamos ter as classes "nome" e "sobrenome", outra classe cpf, outra classe endereço, etc... No final a gente compõe o "Cliente" usando todas essas classes.

Essa seria uma boa prática de programação, do contrário, se eu crio "Cliente", que tem tudo na mesma classe, essa seria uma má prática de programação.

Vamos falar mais sobre isso na seção de padrões  de projeto.
"""