import logging
from util import logcfg
from typing import Tuple


def saludo_doble(name1: str, name2: str) -> Tuple[str, str]:
    return saludo_individual(name1), saludo_individual(name2)


def saludo_individual(name: str) -> str:
    saludo = f"Hola, {name}"
    return saludo


def main() -> None:
    logging.info(saludo_individual("Mayte"))
    logging.info(saludo_doble("Cristina", "Irene"))


if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    main()
    logging.debug("Fin de programa")
