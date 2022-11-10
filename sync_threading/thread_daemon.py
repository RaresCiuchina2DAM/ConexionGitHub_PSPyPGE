import logging
from util import logcfg
import time
import threading
import sys

def heartbeat():
    while True:
        time.sleep(2)
        logging.info("Latido")

def main():
    daemon_thread = threading.Thread(target=heartbeat, daemon=True)
    daemon_thread.start()
    time.sleep(10)
    logging.info("Se termina el thread principal")

if __name__ == "__main__":
    logcfg(__file__)
    logging.debug('Programa iniciado')
    main()
    logging.debug('Programa terminado')