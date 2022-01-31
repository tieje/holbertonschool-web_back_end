#!/usr/bin/python3
'''8. Complex types - functions'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Return a function that multiplies itself'''
    return(lambda x: x * multiplier)
