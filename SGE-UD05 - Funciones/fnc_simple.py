import logging
from util import logcfg


def saludo_doble(name1, name2):
    return saludo_individual(name1), saludo_individual(name2)


def saludo_individual(name):
    """
    The saludo_individual function greets a person by name.

    :param name: Pass the name of the person to whom we want to say hello
    :return: A string
    :doc-author: Trelent
    """
    """
    La función saludo_individual saluda a una persona por su nombre."""
    saludo = f"Hola, {name}"
    return saludo


def main():
    logging.info(saludo_individual("Mayte"))
    logging.info(saludo_doble("Cristina", "Irene"))


if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    main()
    logging.debug("Fin de programa")
