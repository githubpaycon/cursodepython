class Agenda:
    def __init__(self, tarefa) -> None:
        self.tarefa = tarefa
        self.assuntos = []
        
    def add_assunto_da_tarefa(self, assunto):
        self.assuntos.append(Assunto(assunto))
        
    def ver_tarefas_e_assuntos(self):
        print(f'A tarefa a fazer é {self.tarefa}')
        for assunto in self.assuntos:
            print('     '+assunto.assunto)
        else:
            print()

class Assunto:
    def __init__(self, assunto) -> None:
        self.assunto = assunto
