import asyncio
import logging
from util import logcfg


async def hola (nombre):
    logging.info(f"Hola{nombre}")
    return 0

async def main():
    logging.info("Creo la tarea Hola")

    [asyncio.create_task (hola("Mirimi")) for _ in range(10)]


if __name__ in "__main__":
    logcfg(__file__)