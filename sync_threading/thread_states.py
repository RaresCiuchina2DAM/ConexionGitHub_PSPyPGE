import logging
from util import logcfg
import time
import threading


def thread_worker():
    logging.info("En ejecución (running)")
    time.sleep(10)
    logging.info("Acabando el thread")


def main():
    # Se crea una tarea que ejecutará la función thread_worker
    my_thread = threading.Thread(target=thread_worker)
    logging.info(f"my_thread en estado nuevo (new)")

    # Se ordena que el sistema operativo asigne recursos
    # y quede en estado de "listo". Eventualmente empezará
    # a correr
    my_thread.start()

    #E Espera a que la tarea termine
    my_thread.join()
    logging.info("my_thread ha pasado al estado de finalizado (dead)")
    

if __name__ == "__main__":
    logcfg(__file__)
    logging.debug('Programa iniciado')
    main()
    logging.debug('Programa terminado')