import logging
import asyncio
from util import async_timed, logcfg

@async_timed()
async def delay(secs: int) -> int:
    logging.debug(f'durmiendo durante {secs} segundo(s)')
    await asyncio.sleep(secs)
    logging.debug(f'Terminando el sueño de {secs} segundo(s)')
    return f"Dormido durante {secs} segundos"

 
@async_timed()
async def main():
    t1 = asyncio.create_task(delay(2))
    t2 = asyncio.create_task(delay(3))
    await t1
    logging.info(f"t1.result() = {t1.result()}")
    
    await t2
    logging.info(f"t2.result() = {t2.result()}")

if __name__ == "__main__":
    logcfg(__file__)
    asyncio.run(main())