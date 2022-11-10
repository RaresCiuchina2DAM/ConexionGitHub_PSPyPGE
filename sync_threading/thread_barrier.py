import logging
from util import logcfg
from threading import Thread, Barrier
from queue import Queue
import random
import time

def thread_work(bar, q):
    logging.info(f"El primer_paso es {q.get()}")
    time.sleep(random.random()*5)
    bar.wait()
    logging.info(f"El segundo paso es {q.get()}")  
    time.sleep(random.random()*5)
        
def main():
    num_workers = 4
    bar = Barrier(num_workers + 1)
    q = Queue()
    tasks = [Thread(target=thread_work, args=(bar,q)) for _ in range(num_workers)]
    for t in tasks: t.start()
    for i in range(num_workers): q.put("Primer paso")
    bar.wait()
    for i in range(num_workers): q.put("Segundo paso")
    for t in tasks: t.join()
    
if __name__ == '__main__':
    logcfg(__file__)
    logging.debug('Programa iniciado')
    main()
    logging.debug('Programa terminado')