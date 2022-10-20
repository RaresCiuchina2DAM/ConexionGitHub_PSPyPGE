import logging
from util import logcfg
from asyncio import Future
 
def main():
    logging.info('Creando futuro my_f')
    my_f = Future()
    
    logging.info(f'my_f.done() =  {my_f.done()}')

    logging.info('Poniendo 42 en my_f (my_f.set(42))')    
    my_f.set_result(42)
    
    logging.info(f'my_f.done() =  {my_f.done()}')
    logging.info(f'my_f.result() =  {my_f.result()}')

if __name__ ==  '__main__':
    logcfg(__file__)
    logging.debug('Inicio de programa')

    main()
    logging.debug('Inicio de programa')
 