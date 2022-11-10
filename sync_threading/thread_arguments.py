import logging
from util import logcfg
import time
import threading
import random

def thread_worker(i):
    logging.info(f"Thread {i} iniciado")
    time.sleep(random.random()*10)
    logging.info(f"Acabando el thread {i}")

def main():
    threads = [threading.Thread(target=thread_worker,
                                args=(i,)) for i in range(10)]
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