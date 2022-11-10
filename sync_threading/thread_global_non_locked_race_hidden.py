import logging
from util import logcfg
from threading import Thread
import random
import time

counter = 0

def increment_counter():
    global counter
    c = counter
    counter = c+1
    
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

