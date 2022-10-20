import logging
from util import logcfg, delay
import asyncio
 
async def main():
    MAX_PATIENCE = 5 # Paciencia máxima
    long_task = asyncio.create_task(delay(10))
 
    seconds_elapsed = 0
 
    while not long_task.done():
        logging.info('No ha acabado. Esperando otro segundo')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == MAX_PATIENCE:
            # Al cancelar la tarea, la siguiente llamada a 
            # long_task.done() devolverá true y, al hacer
            # await, se levantará CancelledError
            long_task.cancel()
 
    try:
        await long_task
    except asyncio.CancelledError:
        logging.warning('La tarea ha sido cancelada')

if __name__ == '__main__':
    logcfg(__file__)
    logging.debug("Programa iniciado")
    asyncio.run(main())
    logging.debug("Programa terminado")