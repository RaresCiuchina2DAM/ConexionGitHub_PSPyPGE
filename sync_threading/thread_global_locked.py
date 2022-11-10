import logging
from util import logcfg
from threading import Thread, Lock
import random
import time

counter = 0
counter_lock = Lock()

def increment_counter():
    global counter, counter_lock
    counter_lock.acquire()
    c = counter
    time.sleep(0.0001)
    counter = c+1
    counter_lock.release()
    
def main():
    tasks = [Thread(target=increment_counter) for _ in range(100)]
    for t in tasks: t.start()
    for t in tasks: t.join()
    logging.info(f"El valor del contador es {counter}")
    
if __name__ == '__main__':
    logcfg(__file__)
    logging.debug('Programa iniciado')
    main()
    logging.debug('Programa terminado')
