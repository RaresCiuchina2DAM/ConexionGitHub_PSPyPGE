import logging
from util import logcfg
from threading import Thread, Event
import random
import time

number = 0

def producer(ev):
    global number
    time.sleep(random.randint(3,5)*random.random())
    number = random.randint(100,200)
    ev.set()

def consumer(ev):
    global number
    ev.wait()
    logging.info(f"El consumidor encuentra number con el valor {number}")
        
def main():
    number_ready = Event()
    tasks = [Thread(target=producer, args=(number_ready,)), 
             Thread(target=consumer, args=(number_ready,))]
    for t in tasks: t.start()
    for t in tasks: t.join()
    
if __name__ == '__main__':
    logcfg(__file__)
    logging.debug('Programa iniciado')
    main()
    logging.debug('Programa terminado')