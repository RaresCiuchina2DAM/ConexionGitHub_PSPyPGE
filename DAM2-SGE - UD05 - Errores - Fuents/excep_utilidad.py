import logging
from util import logcfg
from datetime import datetime

FORMATS = ["%d/%m/%y",  "%d-%m-%Y", "%d/%m/%Y",
           "%d del %m de %Y",
           "%d%m%y", "%d%m%Y"]

def get_date(date_str):
    for format in FORMATS:
        try:
            input_date = datetime.strptime(date_str, format)
        except Exception as err:
            pass
        else:
            return input_date.strftime("%Y-%m-%d")
    return None

def main():
    while True:   
        d = input("Introduce una fecha: ")
        dnormal = get_date(d)
        if dnormal != None:
            logging.info(f"La fecha normalizada es {dnormal}")
        else:
            logging.info(f"Lo siento, no entiendo la fecha") 

if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    main()
    logging.debug("Fin de programa")
