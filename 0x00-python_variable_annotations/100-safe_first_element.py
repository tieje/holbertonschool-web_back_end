#!/usr/bin/env python3
'''10. Duck typing - first element of a sequence'''
from typing import Sequence


def safe_first_element(lst: Sequence):
    '''Return first element of sequence or None'''
    if lst:
        return lst[0]
    else:
        return None
