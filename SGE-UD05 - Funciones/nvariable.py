import logging
from util import logcfg


def saludo_multiple(principal, *secundarios):
    return (saludo_individual(principal),) + \
           tuple(saludo_individual(n) for n in secundarios)


def saludo_individual(name):
    saludo = f"Hola, {name}"
    return saludo


def suma(*nums):
    # return sum(nums)
    resultado = 0
    for n in nums:
        resultado += n
    return resultado


def main():
    for s in saludo_multiple("Cristina",
                             "Irene",
                             "Mayte",
                             "Manolo"):
        logging.info(f"{s}")
    print(suma(1, 2, 3, 4, 5, 4, 3, 2))
    print(suma())


if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    main()
    logging.debug("Fin de programa")
