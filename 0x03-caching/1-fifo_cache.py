#!/usr/bin/python3
'''1. FIFO caching'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO Cache'''

    def put(self, key: str, item: str) -> None:
        '''
        Assign cache key to value
        If max items is reached, the first item put in will be removed.
        '''
        if BaseCaching.checkArgsIsNone(key, item):
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstKey: str = list(self.cache_data.keys())[0]
            print('DISCARD: ' + firstKey)
            del self.cache_data[firstKey]
