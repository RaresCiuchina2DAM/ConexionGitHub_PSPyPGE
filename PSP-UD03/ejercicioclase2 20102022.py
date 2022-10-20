# Jugador tira tres dados, y cuando termina el primero en hacelo, se declara jugador
import asyncio
import logging
import random

from util import logcfg

TIEMPOSEG = 5

N_veces = 3
dado = [x for x in range(1, 7)]


def tirarDados():
    random.randint(1, 6)


async def jugador(id, f):
    global resultado
    time = round(random.random() * TIEMPOSEG, 4)
    await asyncio.sleep(time)
    for _ in range(N_veces):
        resultado += tirarDados()

    logging.debug(f"El jugador {id} ha esperado {time} .s y tiene de resultado {resultado}")

    if not f.done():
        f.set_result(id, f)
    return f"El jugador {id} ha tardado {time}"


async def main():
    f = asyncio.Future()
    # Se define un array con 100 tareas
    tareas = [asyncio.create_task(jugador(i, f)) for i in range(100)]
    await f
    logging.info(f"El ganador ha sido {f.result()}")


if __name__ == '__main__':
    logcfg(__file__)
    logging.debug('Inicio de programa')
    asyncio.run(main())
    logging.debug('Final del programa')
