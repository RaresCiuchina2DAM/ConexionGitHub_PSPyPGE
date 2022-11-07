import asyncio
import logging
import random

from util import logcfg


# Fabricar las partes del coche que deeemos(ruedas, motor o chasis como objeto)
async def fabPartes(entradaFabrica, objeto):
    while True:
        await asyncio.sleep(num)
        await entradaFabrica.put(objeto)


# Fabricar coches
async def fabricaCoches(entradaFabrica, salidaFabrica):
    numRuedas = 0
    numChasis = 0
    numMotor = 0

    while True:
        # Recoger de la cola un elemento y ver si es chasis, motor o ruedas infinitamente.
        cola = await entradaFabrica.get()
        while cola == "chasis" or cola == "ruedas" or cola == "motor":
            if cola == "chasis":
                numChasis += 1
            if cola == "ruedas":
                numRuedas += 1
            if cola == "motor":
                numMotor += 1
        # Ver si tiene las partes necesarias para crear un coche, en caso de no ser asi, al ser un bucle infinito
        # volverá a recoger elementos hasta que tenga.

        if numMotor >= 1 and numRuedas >= 1 and numMotor >= 1:
            await asyncio.sleep(num)
            logging.info(f"Coche Fabricado")
            numChasis -= 1
            numMotor -= 1
            numRuedas -= 1
            # Manda a la cola salidaFabrica el coche ya montado
            await salidaFabrica.put("coche")
            logging.info(f"Coche mandado a concesionario")


async def concesionario(salidaFabrica):
    # Recogemos de la cola salidaFabrica un elemento y lo guardamos en el array.
    # Cada vez que añadamos un coche, mostraremos mensaje de "Coche en Concesionario"
    cola = await salidaFabrica.get()
    coches_En_Concesionario = []
    for i in coches_En_Concesionario:
        logging.info(f"Coche en Concesionario")
        coches_En_Concesionario[i] = cola


entradaFabrica = asyncio.Queue()
salidaFabrica = asyncio.Queue()
num = random.randint(0, 1)


async def main():
    # Creamos las tareas para fabricar cada una de las partes
    t1 = asyncio.create_task(fabPartes(entradaFabrica, "chasis"))
    t2 = asyncio.create_task(fabPartes(entradaFabrica, "motor"))
    t3 = asyncio.create_task(fabPartes(entradaFabrica, "ruedas"))
    # Llamamos a la funcion para fabricar los coches
    await fabricaCoches(entradaFabrica, salidaFabrica)
    # Paramos las tareas y la fabricacion a los 30 segundos
    await asyncio.sleep(30)
    #Llamamos al concesionario
    await concesionario(salidaFabrica)


if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Inicio de programa")
    asyncio.run(main())
    logging.debug("Fin de programa")
