import logging
from util import logcfg
from threading import Thread, Condition
import random
import time

number = 0

def producer(c):
    global number
    for _ in range(100):
        time.sleep(random.randint(3,5)*random.random()*0.1)
        with c:
            number = random.randint(100,200)
            c.notify()

def consumer(c):
    global number
    with c:
        c.wait()
        logging.info(f"El consumidor encuentra number con el valor {number}")
        
def main():
    number_ready = Condition()
    tasks = [Thread(target=producer, args=(number_ready,))] + \
            [Thread(target=consumer, args=(number_ready,)) for _ in range(100)]
    for t in tasks: t.start()
    for t in tasks: t.join()
    
if __name__ == '__main__':
    logcfg(__file__)
    logging.debug('Programa iniciado')
    main()
    logging.debug('Programa terminado')