import logging
import random
from util import logcfg
import time
from multiprocessing import Queue, Process


# Funcion que crea las ruedas
def fabrica_ruedas(entrada_fabrica):
    while True:
        logcfg(__file__)
        tiempo = random.uniform(0, 1)
        time.sleep(tiempo)

        logging.info(f"Creacion de ruedas ")
        entrada_fabrica.put("ruedas")


# Funcioon que crea el chasis,
def fabrica_chasis(entrada_fabrica):
    while True:
        logcfg(__file__)
        tiempo = random.uniform(0, 1)
        time.sleep(tiempo)

        logging.info(f"Creacion de chasis ")
        entrada_fabrica.put("chasis")


# funcion que crea el motor
def fabrica_motor(entrada_fabrica):
    while True:
        logcfg(__file__)
        tiempo = random.uniform(0, 1)
        time.sleep(tiempo)

        logging.info(f"Creacion de motor ")
        entrada_fabrica.put("motor")


# Funcion de la Fabrica para entrada y salida de la fábrica
def fabrica1(entrada_fabrica, salida_fabrica):
    logcfg(__file__)

    ruedas = 0
    motor = 0
    chasis = 0

    # Mientras sea verdad, veremos si son ruedas, chasis o motor
    while True:
        recogidaDePiezas = entrada_fabrica.get()
        if recogidaDePiezas == "ruedas":
            ruedas += 1
        if recogidaDePiezas == "chasis":
            chasis += 1
        if recogidaDePiezas == "motor":
            motor += 1

        # Y cuando haya piezas de los tres, crearemos el coche
        if ruedas > 0 and chasis > 0 and motor > 0:
            t = random.uniform(0, 1)
            time.sleep(t)
            ruedas = - 1
            chasis = - 1
            motor = - 1
            logging.info(f"Coche fabricado ")
            salida_fabrica.put("coche")


# Funcion del concesionario
# Mientras que sea verdad, mandaremos el coche al concesionario.
def concesionario1(salida_fabrica):
    logcfg(__file__)
    while True:
        t = random.uniform(0, 1)
        time.sleep(t)
        salida_fabrica.get()
        if salida_fabrica.get() == "coche":
            logging.info("Coche en concesionario")


def main():
    # Creamos las colas entrada_fabrica y salida_fabrica
    entrada_fabrica = Queue()
    salida_fabrica = Queue()

    ruedas = Process(target=fabrica_ruedas, args=(entrada_fabrica,))
    motor = Process(target=fabrica_motor, args=(entrada_fabrica,))
    chasis = Process(target=fabrica_chasis, args=(entrada_fabrica,))
    fabrica = Process(target=fabrica1, args=(entrada_fabrica, salida_fabrica))
    concesionario = Process(target=concesionario1, args=(salida_fabrica,))

    # Iniciamos los procesos creados de antes uno a uno
    ruedas.start()
    motor.start()
    chasis.start()
    fabrica.start()
    concesionario.start()

    # Esperamos 30 segundos que es la duración del programa
    time.sleep(30)

    # Terminamos los procesos creados antes, dado que han pasado los 30 segundos.
    ruedas.terminate()
    motor.terminate()
    chasis.terminate()
    fabrica.terminate()
    concesionario.terminate()


if __name__ == "__main__":
    logcfg(__file__)
    logging.debug('Inicio')
    main()
    logging.debug("Final")
