import logging
from util import logcfg

def saludo_cuadruple(name1, name2, name3, name4):
    return saludo_individual(name1), \
           saludo_individual(name2), \
           saludo_individual(name3), \
           saludo_individual(name4)

def saludo_individual(name):
    saludo = f"Hola, {name}"
    return saludo

def main():
    for s in saludo_cuadruple("Cristina", 
                              "Irene", 
                              "Mayte",
                              "Manolo"):
        logging.info(f"{s}")

if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    main()
    logging.debug("Fin de programa")