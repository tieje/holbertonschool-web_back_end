#!/usr/bin/env python3
'''0. Simple helper function'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[(int, int)]:
    '''Return tuple of start and end page'''
    end: int = page * page_size
    start: int = end - page_size
    res = (start, end)
    return res
