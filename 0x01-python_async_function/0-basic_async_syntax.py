#!/usr/bin/env python3
'''0. The basics of async'''

from random import random
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    '''Return delay'''
    delay: float = random() * max_delay
    await sleep(delay)
    return delay
