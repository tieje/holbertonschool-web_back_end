#!/usr/bin/env python3
'''2. Measure the runtime'''
import asyncio
from typing import Callable
from time import time, perf_counter

wait_n: Callable = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Return the time it takes to run wait_n async func'''
    # start: float = time()
    start: float = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    # end: float = time()
    end: float = perf_counter()
    return end - start
