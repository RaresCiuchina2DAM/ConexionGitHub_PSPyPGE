import logging
import asyncio
from asyncio import Queue
from util import logcfg, delay
import random

TMAXLLEGADA = 100_000
TMAXATENCION = 4_000
NUMCLIENTES = 200
NUMCAJEROS = 4

async def cajero(id, q):
    while True:
        try:
            clid = await q.get()
            logging.info(f"Cajero {id} atiende a cliente {clid}")
            logging.info(f"Longitud de la cola: {q.qsize()}")
            await delay (random.randint(10, TMAXATENCION)/1000)
            logging.info(f"Cajero {id} acaba de atender a cliente {clid}")

        except Exception as e:
            logging.info(f"Cajero {id} es interrumpido")
            break


async def cliente(id, q):
    await delay(random.randint(10, TMAXLLEGADA)/1000)
    logging.info(f"Cliente {id} llega a la cola")
    await q.put(id)
    logging.info(f"Longitud de la cola: {q.qsize()}")

async def main():
    q = Queue()
    clientes = [asyncio.create_task(cliente(i,q)) for i in range(NUMCLIENTES)]
    cajeros = [asyncio.create_task(cajero(i,q)) for i in range(NUMCAJEROS)]
    await asyncio.gather(*clientes)
    while not q.empty():
        await delay(1)
    for cj in cajeros:
        cj.cancel()
    q.task_done()
    # await q.join()

if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    asyncio.run(main())
    logging.debug("Fin de programa")