import asyncio
import logging

from util import logcfg


async def Pinger(pingq, pongq):
    while True:
        await asyncio.sleep(1)
        await pingq.put("Ping")
        pong = await pongq.get()
        logging.info(f"{pong} esta recibido")


async def Ponger(pingq, pongq):
    while True:
        ping = await pingq.get()
        logging.info(f"{ping} esta recibido")
        await asyncio.sleep(1)
        await pongq.put("Pong")


async def main():
    pingq = asyncio.Queue()
    pongq = asyncio.Queue()
    t1 = asyncio.create_task(Pinger(pingq, pongq))
    t2 = asyncio.create_task(Ponger(pingq, pongq))
    await asyncio.sleep(30)


if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Inicio de programa")
    asyncio.run(main())
    logging.debug("Fin de programa")
