import logging
import asyncio

import sys
from util import delay, logcfg

async def add_one(number: int) -> int:
    """Función asíncrona que suma uno al número que se le pasa utilizando

    Args:
        number (int): _description_

    Returns:
        int: número que se le pasa
    """    
    return number + 1
 
async def hello_world_message() -> str:
    """Devuelve un mensaje de bienvenida

    Returns:
        str: _description_
    """    
    await delay(1)
    return 'Hello World!'
 
async def main() -> None:
    """Función asíncrona que se ejecuta con el módulo
    """    
    message = await hello_world_message() 
    one_plus_one = await add_one(1)
    logging.info(f"El resultado de llamar a add_one(1) es {one_plus_one}")
    logging.info(message)

if __name__ == '__main__':
    logcfg(__file__)
    logging.info(sys.path)
    asyncio.run(main())