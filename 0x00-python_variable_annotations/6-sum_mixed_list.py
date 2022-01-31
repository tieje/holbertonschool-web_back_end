#!/usr/bin/python3
'''6. Complex types - mixed list'''
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''Return sum of list int and floats'''
    return(sum(mxd_list))
