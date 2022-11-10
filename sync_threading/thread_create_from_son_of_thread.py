import logging
from util import logcfg
import time
import threading
import random

class ThreadWorker(threading.Thread):
    def run(self):
        logging.info("Thread iniciado")
        time.sleep(random.random()*10)
        logging.info("Acabando el thread")

def main():
    threads = [ThreadWorker() for _ in range(10)]
    for t in threads: t.start()
    while threads:
        time.sleep(0.2)
        for t in threads:
            if not t.is_alive():
                t.join()
                threads.remove(t)
    logging.info("Todas las tareas han acabado")   

if __name__ == "__main__":
    logcfg(__file__)
    logging.debug('Programa iniciado')
    main()
    logging.debug('Programa terminado')