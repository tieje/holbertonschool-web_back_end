#!/usr/bin/env python3
'''4. Tasks'''
from typing import Callable, List
import asyncio

task_wait_random: Callable = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Return tasks as completed in that order'''
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
