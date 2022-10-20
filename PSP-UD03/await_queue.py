import logging
from util import logcfg
from asyncio import Queue
import asyncio
import random
 
async def producer(q, n):
    for i in range(n):
        await asyncio.sleep(random.randint(1,10))
        logging.info(f"Productor produce {i}")
        await q.put(i)

async def consumer(q, n):
    for _ in range(n):
        c = await q.get()
        await asyncio.sleep(random.randint(1, 10))
        logging.info(f"Consumidor consume {c}")
    

async def main():
    q = Queue()
    NPRODUCTS = 5
    p = asyncio.create_task(producer(q, NPRODUCTS))
    c = asyncio.create_task(consumer(q, NPRODUCTS))
    await asyncio.gather(p,c)


if __name__ ==  '__main__':
    logcfg(__file__)
    logging.debug('Inicio de programa')

    asyncio.run(main())

    logging.debug('Fin de programa')
 