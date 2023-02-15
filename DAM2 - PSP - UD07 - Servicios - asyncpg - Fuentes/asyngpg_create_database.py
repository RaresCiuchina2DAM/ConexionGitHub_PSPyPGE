from util import logcfg
import logging
import asyncpg
import asyncio
from datetime import datetime

CREATE_BD_PRODUCTS = """
CREATE DATABASE products;
"""

async def main():
    connection = await asyncpg.connect(host='192.168.56.217',
                                       port=5432,
                                       user='postgres',
                                       database='postgres',
                                       password='postgres')
    version = connection.get_server_version()
    logging.info(f'¡Conectado! Postgres, version {version}')
    status = await connection.execute(CREATE_BD_PRODUCTS)
    logging.info(status)
    await connection.close()
 
if __name__ == "__main__":
    stime = datetime.now()
    logcfg(__file__)
    asyncio.run(main())
    logging.info(f"El programa ha tardado {datetime.now()-stime}")