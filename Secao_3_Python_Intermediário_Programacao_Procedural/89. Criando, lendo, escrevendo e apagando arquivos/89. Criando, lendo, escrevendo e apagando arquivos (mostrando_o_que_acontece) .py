file = open('abc.txt', 'w+')  # abre ou cria o arquivo, limpa o arquivo em caso de ter algo escrito e abre para escrita e leitura
file.write('linha1\n')  # add linha1
file.write('linha2\n')  # add linha2
file.write('linha3\n')  # add linha3
file.write('linha4\n')  # add linha4
print('mostrando arquivo: \n')  # mostra na tela 'mostrando arquivo e quebra a linha'
file.seek(0, 0)  # coloca o cursor no começo do arquivo para ser lido.
print(file.read())  # faz a impressão do arquivo todinho
file.seek(0, 0)  # depois de ler o arquivo, o cursor volta para o final e tem que colocar o cursor no começo do arquivo
print('#' * 20)  # mostra # 20 vezes
print(file.readline(), end='')  # escreve a 1 linha e mostra so a quebra de linha do arquivo
print(file.readline(), end='')  # escreve a 2 linha e mostra so a quebra de linha do arquivo
print(file.readline(), end='')  # escreve a 3 linha e mostra so a quebra de linha do arquivo
file.close()
