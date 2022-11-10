import asyncio
import logging
import random

from util import logcfg


# Fabricar las partes del coche que deesemos(ruedas, motor o chasis como objeto)
async def fabPartes(entradaFabrica, objeto):
    while True:
        await asyncio.sleep(random.randint(0, 1))
        await entradaFabrica.put(objeto)


# Fabricar coches
async def fabricaCoches(entradaFabrica, salidaFabrica):
    numRuedas = 0
    numChasis = 0
    numMotor = 0

    while True:
        # Recoger de la cola un elemento y ver si es chasis, motor o ruedas infinitamente.
        cola = await entradaFabrica.get()
        # while cola == "chasis" or cola == "ruedas" or cola == "motor":
        if cola == "chasis":
            numChasis += 1
        if cola == "ruedas":
            numRuedas += 1
        if cola == "motor":
            numMotor += 1
        # Ver si tiene las partes necesarias para crear un coche,
        # en caso de no ser asi, al ser un bucle infinito
        # volverá a recoger elementos hasta que tenga.

        if numMotor >= 1 and numRuedas >= 1 and numMotor >= 1:
            await asyncio.sleep(random.randint(0, 1))
            logging.info(f"Coche Fabricado")
            numChasis -= 1
            numMotor -= 1
            numRuedas -= 1
            # Manda a la cola salidaFabrica el coche ya montado
            await salidaFabrica.put("coche")


async def concesionario(salidaFabrica):
    # Recogemos de la cola salidaFabrica un elemento y lo guardamos en el array.
    # Cada vez que añadamos un coche, mostraremos mensaje de "Coche en Concesionario"

    while True:
        await salidaFabrica.get()
        logging.info(f"Coche en Concesionario")


async def main():
    entradaFabrica = asyncio.Queue()
    salidaFabrica = asyncio.Queue()

    # Creamos las tareas para fabricar cada una de las partes
    t1 = asyncio.create_task(fabPartes(entradaFabrica, "chasis"))
    t2 = asyncio.create_task(fabPartes(entradaFabrica, "motor"))
    t3 = asyncio.create_task(fabPartes(entradaFabrica, "ruedas"))
    # Creamos la tarea para fabricar los coches
    t4 = asyncio.create_task(fabricaCoches(entradaFabrica, salidaFabrica))
    # Creamos la tarea para el concesionario, que contiene
    # el bucle infinito para recoger los coches
    # y mostrar el mensaje de "Coche en Concesionario"
    t5 = asyncio.create_task(concesionario(salidaFabrica))

    # Paramos todas las tareas creadas anteriormente, tras 30 seg de ejecucion
    await asyncio.sleep(30)
    t1.cancel()
    t2.cancel()
    t3.cancel()
    t4.cancel()




if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Inicio de programa")
    asyncio.run(main())
    logging.debug("Fin de programa")
