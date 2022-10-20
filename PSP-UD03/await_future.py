import logging
from util import logcfg
from asyncio import Future
import asyncio
import random
 
async def producer(f):
    await asyncio.sleep(random.randint(1,5))
    f.set_result(random.randint(0,100))
    logging.info("Acaba el trabajo del productor")

async def consumer(f):
    logging.info("Cliente esperando que el productor produzca")
    value = await f
    logging.info(f"El consumidor ya tiene el número {value}")

async def main():
    f = asyncio.Future()
    await asyncio.gather(producer(f), consumer(f))


if __name__ ==  '__main__':
    logcfg(__file__)
    logging.debug('Inicio de programa')
    asyncio.run(main())
    logging.debug('Fin de programa')
 