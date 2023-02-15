import asyncio
import logging
# from logs_functions import logcfg
 
 
async def delay(delay_seconds: int) -> int:
    logging.debug(f'Durmiendo durante {delay_seconds} segundo(s)')
    await asyncio.sleep(delay_seconds)
    logging.debug(f'Sueño finalizado de  {delay_seconds} segundo(s)')
    return delay_seconds

if __name__ == "__main__":
    logcfg(__file__)
    logging.info("Comienza programa")
    asyncio.run(delay(2))
    asyncio.run(delay(3))
    logging.info("Finaliza programa")