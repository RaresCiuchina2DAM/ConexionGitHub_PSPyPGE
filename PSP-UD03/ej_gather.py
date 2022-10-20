import logging
from util import logcfg
import asyncio
import random


async def runner(id):
    # El corredor va a tardar un tiempo aleatorio entre 0 y 10 s
    time = round(random.random() * 10, 3)
    await asyncio.sleep(time)
    logging.debug(f'runner({id}) ha esperado {time} s.')
    # Cada runner devuelve el id y el tiempo empleado
    return (id, time)


async def main():
    # Se define un array con 100 tareas
    tasks = [runner(i) for i in range(100)]
    # gather sirve para arrancar las tareas y esperar los resultados
    results = await asyncio.gather(*tasks)
    logging.info(f'Resultados ordenados por id: {results}')


if __name__ == '__main__':
    logcfg(__file__)
    logging.debug('Inicio de programa')
    asyncio.run(main())
    logging.debug('Inicio de programa')
