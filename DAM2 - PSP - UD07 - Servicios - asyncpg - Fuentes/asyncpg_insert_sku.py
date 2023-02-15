from util import logcfg
import logging
import asyncpg
import asyncio
from datetime import datetime
import os
import random

BRANDS_FILE = os.path.join(os.path.dirname(__file__),'marcas.txt')

async def generate_skus(con, nskus):
    product_query = 'SELECT product_id FROM product'
    products = await con.fetch(product_query)
    skus = []
    for _ in range(nskus):
        product = random.choice(products)
        size_id = random.randint(1,3)
        color_id = random.randint(1,2)
        skus.append((product['product_id'],
                     size_id,
                     color_id))
    return skus

async def main():
    connection = await asyncpg.connect(host='192.168.56.217',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres')
    skus = await generate_skus(connection, 100_000)
    await connection.executemany(
        "INSERT INTO sku (product_id, product_size_id, product_color_id) "
        "VALUES ($1, $2, $3);",
        skus)
    await connection.close()
    
if __name__ == "__main__":
    stime = datetime.now()
    logcfg(__file__)
    asyncio.run(main())
    logging.info(f"El programa ha tardado {datetime.now()-stime}") 