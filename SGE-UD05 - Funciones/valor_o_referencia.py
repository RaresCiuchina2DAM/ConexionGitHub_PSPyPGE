import logging
from util import logcfg

def print_id(d, n, s):
    n = 4
    d["primero"] = "trabajar"
    s = "Noche"
    logging.info(f"En print_id: {id(d)} {id(n)} {id(s)}")


def main() -> None :
    d = {"primero": "vivir", "después": "filosofar" }
    n = 35
    s = "Día"
    logging.info(f"En main: {id(d)} {id(n)}  {id(s)}")
    print_id(d, n, s)

if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    main()
    logging.debug("Fin de programa")