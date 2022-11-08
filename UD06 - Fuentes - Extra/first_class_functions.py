import logging
from util import logcfg

def create_conversor(factor):
    def cfact(x):
        return x*factor
    
    return cfact


def main():
    euro_dollar_change = 1.01
    change_to_euros = create_conversor(euro_dollar_change)

    c_in_dollars = [100.0, 187.25, 299.99, 3_000_0000]
    for c in c_in_dollars:
        logging.info(round(change_to_euros(c),2))
   
if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    main()
    logging.debug("Fin de programa")