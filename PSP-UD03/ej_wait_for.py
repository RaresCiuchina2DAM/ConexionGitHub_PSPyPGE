import logging
from util import logcfg, delay
import asyncio
 
async def main():
    MAX_PATIENCE = 5 # Paciencia máxima
    long_task = asyncio.create_task(delay(10))
 
    seconds_elapsed = 0
 
    try:
        await asyncio.wait_for(long_task, timeout=5)
    except asyncio.TimeoutError:
        logging.warning('Ha vencido el temporizador')

if __name__ == '__main__':
    logcfg(__file__)
    logging.debug("Programa iniciado")
    asyncio.run(main())
    logging.debug("Programa terminado")