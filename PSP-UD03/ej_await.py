import logging
import asyncio
from util import logcfg

async def add_one(n):
    return n + 1

async def main():
    result1 = await add_one(1)
    logging.info(f"result1 = {result1}")
    
    result2 = await add_one(100)
    logging.info(f"result2 = {result2}")

 
if __name__ == "__main__":
    logcfg(__file__)
    logging.debug(f"Comenzado programa {__file__}")
    asyncio.run(main())
    logging.debug(f"Finalizando programa {__file__}")
    
    