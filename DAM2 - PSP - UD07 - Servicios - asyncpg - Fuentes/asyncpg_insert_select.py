from util import logcfg
import logging
import asyncpg
import asyncio
from datetime import datetime


async def main():
    connection = await asyncpg.connect(host='192.168.56.217',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres')
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")
    # await connection.execute("DELETE FROM brand WHERE brand_name='Levis'")
    # await connection.execute("DELETE FROM brand WHERE brand_name='Seven'")

    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results = await connection.fetch(brand_query)

    for brand in results:
        logging.info(f'bramd_id: {brand["brand_id"]},'
                     f'  brand_name: {brand["brand_name"]}')

    await connection.close()


if __name__ == "__main__":
    stime = datetime.now()
    logcfg(__file__)
    asyncio.run(main())
    logging.info(f"El programa ha tardado {datetime.now() - stime}")
