import logging
from util import logcfg
from threading import Thread, Semaphore, active_count
from queue import Queue
import random
import time

def thread_work(sem, q):
    with sem:
        q.put("")
        logging.info(f"La cola mide {q.qsize()}")
        time.sleep(0.1)
        q.get()
        
def main():
    sem = Semaphore(4)
    q = Queue()
    tasks = [Thread(target=thread_work, args=(sem,q)) for _ in range(100)]
    for t in tasks: t.start()
    for t in tasks: t.join()
    
if __name__ == '__main__':
    logcfg(__file__)
    logging.debug('Programa iniciado')
    main()
    logging.debug('Programa terminado')