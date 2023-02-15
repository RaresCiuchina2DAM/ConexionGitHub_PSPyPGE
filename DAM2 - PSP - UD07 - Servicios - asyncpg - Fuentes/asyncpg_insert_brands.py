from util import logcfg
import logging
import asyncpg
import asyncio
from datetime import datetime
import os
import random

BRANDS_FILE = os.path.join(os.path.dirname(__file__),'marcas.txt')
NBRANDS = 100

def generate_brand_names(fname,n):
    with open(fname) as f:
        words = [line[:-1] for line in f]
    return [(w,) for w in random.sample(words, n)]

async def main():
    connection = await asyncpg.connect(host='192.168.56.217',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres')
    brands = generate_brand_names(BRANDS_FILE, NBRANDS)
    await connection.executemany(
        "INSERT INTO brand (brand_name) VALUES ($1);",
        brands)
    await connection.close()
    
if __name__ == "__main__":
    stime = datetime.now()
    logcfg(__file__)
    asyncio.run(main())
    logging.info(f"El programa ha tardado {datetime.now()-stime}") 