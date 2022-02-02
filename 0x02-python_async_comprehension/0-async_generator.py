#!/usr/bin/env python3
'''0. Async Generator'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Yield random float 10 times'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
