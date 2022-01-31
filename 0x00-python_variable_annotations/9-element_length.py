#!/usr/bin/python3
'''9. Let's duck type an iterable object'''


from typing import List, Tuple

item = tuple[str, float]
def element_length(lst: List[str]) -> List[Tuple[str, float]]:
    '''Return list of tuples of (item, item length)'''
    return [(i, len(i)) for i in lst]
