import functools
import time
from typing import Callable, Any
import logging
 
 
def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            logging.debug(f'comenzando {func.__name__} con argumentos {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                logging.debug(f'finalizando {func.__name__} en {total:.4f} segundo(s)')
 
        return wrapped
 
    return wrapper