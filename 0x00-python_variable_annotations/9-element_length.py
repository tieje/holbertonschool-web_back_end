#!/usr/bin/env python3
'''9. Let's duck type an iterable object'''


from typing import Iterable, List, Sequence, Tuple

item = Tuple[str, float]


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return list of tuples of (item, item length)'''
    return [(i, len(i)) for i in lst]
