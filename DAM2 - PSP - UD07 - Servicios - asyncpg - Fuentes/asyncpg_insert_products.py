from util import logcfg
import logging
import asyncpg
import asyncio
from datetime import datetime
import os
import random

BRANDS_FILE = os.path.join(os.path.dirname(__file__),'marcas.txt')

async def generate_products(fname, con, nproducts):
    with open(fname) as f:
        words = [line[:-1] for line in f]
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    brands = await con.fetch(brand_query)
    products = []
    for _ in range(nproducts):
        description = random.sample(words, 10)
        brand = random.choice(brands)
        products.append((" ".join(description), brand['brand_id']))
    return products

async def main():
    connection = await asyncpg.connect(host='192.168.56.217',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres')
    products = await generate_products(BRANDS_FILE, 
                                       connection,
                                       1000)
    await connection.executemany(
        "INSERT INTO product (product_name, brand_id) VALUES ($1, $2);",
        products)
    await connection.close()
    
if __name__ == "__main__":
    stime = datetime.now()
    logcfg(__file__)
    asyncio.run(main())
    logging.info(f"El programa ha tardado {datetime.now()-stime}") 