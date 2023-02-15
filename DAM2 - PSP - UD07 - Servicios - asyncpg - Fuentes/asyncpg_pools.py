from util import logcfg
import logging
import asyncpg
import asyncio
from datetime import datetime
import os
import random

product_query = \
    """
SELECT
p.product_id, p.product_name, p.brand_id,
s.sku_id,
pc.product_color_name, ps.product_size_name
FROM product as p
JOIN sku as s on s.product_id = p.product_id
JOIN product_color as pc on pc.product_color_id = s.product_color_id
JOIN product_size as ps on ps.product_size_id = s.product_size_id
WHERE p.product_id = {product_id} ;
   """
 
async def query_product(pool, product_id):
    async with pool.acquire() as connection:
        return await connection.fetch(product_query.format(product_id=product_id))
 
async def main():
    product_query = 'SELECT product_id FROM product'
    async with asyncpg.create_pool(host='192.168.56.217',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres',
                                       min_size=4, max_size=4) as pool:
        async with pool.acquire() as con:
            products = await con.fetch(product_query)
        sel = random.sample(products, 10)
        queries = [query_product(pool, p['product_id']) for p in sel]
        results = await asyncio.gather(*queries)
        for r in results:
            logging.info(r)
    
if __name__ == "__main__":
    stime = datetime.now()
    logcfg(__file__)
    asyncio.run(main())
    logging.info(f"El programa ha tardado {datetime.now()-stime}") 