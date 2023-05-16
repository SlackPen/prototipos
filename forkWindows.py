import multiprocessing
from time import sleep 
from datetime import datetime 
from datetime import timedelta
from random import randint 


    
def worker(idxTask, tempo):
    agora = datetime.now()
    fim   = datetime.now()
    print(idxTask, 'Iniciando esta Task')
    while True:
        if (fim - agora).seconds >= 30:
            break 
        
        sleep(tempo)
        fim   = datetime.now()
        print(idxTask, '........', tempo, datetime.now())
    print(idxTask, 'Encerrando esta Task')

def main():
    tam = randint(5,55)
    lst = [] 
    print('Simularei em 30 segundos a execução de %d Tasks em processamento simultâneo com temporização aleatória para finalização do processo.' % (tam,))
    agora = datetime.now()
    fim   = datetime.now()    
    while True:
        if (fim - agora).seconds >= 30:
            break         
        sleep(.01)
        fim   = datetime.now()
        print('Contando.......:.', fim - agora, end='\r')    
    
    for idxTask in range(tam):
        tempo = randint(10,1000) / 100
        p = multiprocessing.Process(target=worker, args=(idxTask, tempo))        
        p.daemon = True
        p.start()
        lst.append(p)
    
    for i in lst:
        i.join()  

    print('\n MainBot encerrando, %d tarefas concluídas.\n' % (tam,))

if __name__=="__main__":
   main()