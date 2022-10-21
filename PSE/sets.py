from util import logcfg
import logging
import random

LNUMBERS = 1_000_000
MINN = 1
MAXN = 100_000

def main():
    logging.info("Empiezo a crear una lista")
    biglist = [random.randint(MINN, MAXN) for _ in range(LNUMBERS)]
    logging.info(f"Acabo de crear la lista con tamaño {len(biglist)}")
    out_of_biglist = [x for x in range(MINN, MAXN+1) if x not in biglist]
    logging.info(f"La lista de excluidos tiene {len(out_of_biglist)} elementos")

    logging.info("Empiezo a crear un conjunto")
    bigset = {random.randint(MINN, MAXN) for _ in range(LNUMBERS)}
    logging.info(f"Acabo de crear el conjunto con tamaño {len(bigset)}")
    out_of_bigset = {x for x in range(MINN, MAXN+1) if x not in bigset}
    logging.info(f"El conjunto de excluidos tiene {len(out_of_bigset)} elementos")



if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Programa iniciado")
    main()
    logging.debug("Programa finalizado")