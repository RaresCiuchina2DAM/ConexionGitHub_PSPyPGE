import logging
from util import logcfg
import asyncio
import random

productos = {"manzanas": 2.3, "plátanos": 3.5, "tomates": 2.5}

async def cliente(carrito, cuenta):
    await asyncio.sleep(random.randint(1,5))
    compra = random.sample(productos.keys(),random.randint(1,len(productos)))
    logging.info(f'cliente va a hacer compra: {compra}')
    await carrito.put(compra)
    importe = await cuenta.get()
    logging.info(f"Cliente recibe la cuenta - importe: {importe}")

async def cajero(carrito, cuenta):
    compra = await carrito.get()
    logging.info(f'Cajero tiene que procesar {compra}')
    await asyncio.sleep(random.randint(2,3))
    importe = 0
    for producto in compra:
        importe += productos[producto]
    logging.info(f'Cajero ha calculado el importe: {importe}')
    await cuenta.put(importe)

async def main():
    carrito = asyncio.Queue()
    cuenta = asyncio.Queue()
    tasks = [cliente(carrito, cuenta), cajero(carrito, cuenta)]
    await asyncio.gather(*tasks)
    
if __name__ ==  '__main__':
    logcfg(__file__)
    logging.debug('Inicio de programa')
    asyncio.run(main())
    logging.debug('Final del programa')