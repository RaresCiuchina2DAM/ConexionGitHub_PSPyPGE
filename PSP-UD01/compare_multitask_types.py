import logging
from util import logcfg

import time
from multiprocessing import Process
from threading import Thread
import requests
import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import functools

import aiohttp

REQUESTS = [f'http://192.168.56.203:5000/dec2bin/{x}' for x in range(5_000)] 

def req(url) -> str:
    start = time.time()
    result = requests.get(url)
    end = time.time()
    return result.content
 
def no_tasks(reqs):
    start_time = time.time()
    results = [req(url) for url in reqs]
    logging.debug(f"Monotarea finalizada - results = {results}")
    end_time = time.time()
    logging.info(f'Completada (monotarea) in {end_time-start_time}')


async def pool_tasks(cl, reqs):
    start_time = time.time()
    
    loop = asyncio.get_running_loop()

    logging.info(f"Empleando {cl}")
    with cl() as pool:
        tasks = [loop.run_in_executor(pool, functools.partial(req, url)) 
                    for url in reqs]
        logging.info(f"len(tasks) = {len(tasks)}")
        results = await asyncio.gather(*tasks)
        logging.debug(f"Tareas finalizadas ({cl}) - results = {results}")
    
    end_time = time.time()
    logging.info(f'Completadas ({cl}) en {end_time-start_time}')

async def fetch_content(session, url):
    async with session.get(url) as result:
        return await result.text()

async def with_aiohttp(reqs):
    start_time = time.time()
    
    logging.info(f"Empleando aiohttp")

    async with aiohttp.ClientSession() as session:
        contents = [fetch_content(session, url) for url in reqs]
        results = await asyncio.gather(*contents)
        logging.debug(f"Tareas aiohttp finalizadas - results ={results}")
        
    
    end_time = time.time()
    logging.info(f'Completadas (aiohttp) en {end_time-start_time}')



if __name__ == "__main__":
    logcfg(__file__)
    
    logging.debug("Programa iniciado")

   
    no_tasks(REQUESTS)
    asyncio.run(pool_tasks(ProcessPoolExecutor, REQUESTS))
    asyncio.run(pool_tasks(ThreadPoolExecutor, REQUESTS))
    asyncio.run(with_aiohttp(REQUESTS))
    
    
    logging.debug("Programa terminado")

