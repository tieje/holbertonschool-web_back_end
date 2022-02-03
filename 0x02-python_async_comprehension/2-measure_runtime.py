#!/usr/bin/env python3
'''2. Run time for four parallel comprehensions'''

from typing import Callable
import asyncio
from time import perf_counter
async_comprehension: Callable = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime():
    '''Run for four parallel comprehensions in 10 seconds'''
    start: float = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end: float = perf_counter()
    return end - start
