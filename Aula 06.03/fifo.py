from  collections import deque

class FifoSheduler:
    # inicializador  (Construtor de Classe)
    def __init__(self):
        self.fila_processos = deque()

    def adicionar_processo(self, pid, tempo_exec):
        processo = (pid, tempo_exec)
        self.fila_processos.append(processo)

    def remover_processo(self):
        if self.fila_processos:
            return self.fila_processos.popleft()
        else:
            print("Nenhum processo para remover.")
            return
        
    def fifo_scheduling(self):
        tempo_atual = 0
        tempo_espera = {}
        tempo_retorno = {}

        print ('\n Execução dos processos (FIFO):\n')

        while self.fila_processos:
            pid, tempo_exec = self.remover_processo()

            tempo_espera[pid] = tempo_atual
            tempo_espera[pid]= tempo_atual + tempo_exec

            print (f'Processo {pid} executando ... (Tempo: {tempo_atual} → {tempo_atual + tempo_exec})')

            tempo_atual +=tempo_exec

            print('\n resumo do deslocamento:')
            print ('PID | Tempo de Espera | Tempo de Retorno')
            for pid in tempo_espera:
                print (f'{pid:^3} | {tempo_espera[pid]:^15} | {tempo_retorno[pid]:^14}')


scheduler = FifoSheduler()

scheduler.adicionar_processo(1,5)
scheduler.adicionar_processo(2,3)
scheduler.adicionar_processo(3,8)
scheduler.adicionar_processo(4,6)

scheduler.fifo_scheduling()