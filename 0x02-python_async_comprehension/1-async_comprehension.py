#!/usr/bin/env python3
'''1. Async Comprehensions'''
from typing import Callable, List


async_generator: Callable = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Return a list of floats from async_generator()'''
    return [i async for i in async_generator()]
