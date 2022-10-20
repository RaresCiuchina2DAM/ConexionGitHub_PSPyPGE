# Jugador tira tres dados
import asyncio
import logging
import random

from util import logcfg

TIEMPOSEG = 5

N_veces = 3
dado = [x for x in range(1, 7)]

def tirarDados():
    random.randint(1,6)

async def jugador(id):
    global resultado
    time = round(random.random() * TIEMPOSEG, 4)
    await asyncio.sleep(time)
    for _ in range(N_veces):
        resultado += tirarDados()

    logging.debug(f"El jugador {id} ha esperado {time} .s y tiene de resultado {resultado}")

    return (id,resultado,time)


async def main():
    # Se define un array con 10 tareas
    tareas = [jugador(i) for i in range(10)]
    # gather sirve para arrancar las tareas y esperar los resultados
    resultados = await asyncio.gather(*tareas)
    logging.info(f'Resultados ordenados por id: {resultados}')


if __name__ == '__main__':
    logcfg(__file__)
    logging.debug('Inicio de programa')
    asyncio.run(main())
    logging.debug('Final del programa')
