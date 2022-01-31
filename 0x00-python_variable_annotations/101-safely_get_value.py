#!/usr/bin/env python3
'''11. More involved type annotations'''


def safely_get_value(dct, key, default=None):
    if key in dct:
        return dct[key]
    else:
        return default
