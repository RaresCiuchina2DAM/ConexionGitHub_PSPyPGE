import logging
from util import logcfg
from threading import Thread, Semaphore, active_count
from queue import Queue
import random
import time

def philosopher(sem, q):
    for _ in range(10):
        with sem:
            forks = [q.get() for _ in range(2)]
            logging.info(f"Filósofo comiendo con {forks}")
            time.sleep(random.random())
            for f in forks: q.put(f)
        
def main():
    num_philosophers = 5
    forks = [f"Tenedor {i}" for i in range(num_philosophers)]
    sem = Semaphore(num_philosophers)
    q = Queue()
    tasks = [Thread(target=philosopher, args=(sem,q)) for _ in range(num_philosophers)]
    for f in forks: q.put(f)
    for t in tasks: t.start()
    for t in tasks: t.join()
    
if __name__ == '__main__':
    logcfg(__file__)
    logging.debug('Programa iniciado')
    main()
    logging.debug('Programa terminado')