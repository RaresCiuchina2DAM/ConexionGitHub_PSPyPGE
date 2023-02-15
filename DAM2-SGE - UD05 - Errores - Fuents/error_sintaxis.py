import logging
from util import logcfg


def main():
    nstr = input("Introduce un número entero")
    # La función input devuelve un string, por lo que
    # es ilegal intentar hacer un rango sobre nstr. 
    # En cualquier caso Hay un error sintáctico
    for i in range(nstr) logging.info(i)

if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    main()
    logging.debug("Fin de programa")