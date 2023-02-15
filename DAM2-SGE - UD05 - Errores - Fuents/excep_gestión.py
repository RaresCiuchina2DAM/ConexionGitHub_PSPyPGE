import logging
from util import logcfg


def main():    
    try:
        nstr = input("Introduce un número entero: ")
        for i in range(int(nstr)): logging.info(i)
    except ValueError as terr:
        logging.error(f"Error de valor: {verr}")
    except KeyboardInterrupt as kerr:
        logging.error(f"Error, presionado Ctl-C {kerr}")
    else:
        logging.info(f"Perfecto, no ha habido errores")
    finally:
        logging.info(f"Código que se ejecuta con o sin excepciones")

if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    main()
    logging.debug("Fin de programa")