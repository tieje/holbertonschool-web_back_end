#!/usr/bin/python3
'''1. FIFO caching'''
from base_caching import BaseCaching
from typing import List, Union


class FIFOCache(BaseCaching):
    '''FIFO Cache'''

    def __init__(self):
        '''Add input Order to keep track of order'''
        super().__init__()
        self.__Order: List[str] = []

    def put(self, key: str, item: str) -> None:
        '''
        Assign cache key to value
        If max items is reached, the first item put in will be removed.
        '''
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.__Order:
            lastKey: str = self.__Order.pop(0)
            del self.cache_data[lastKey]
            print('DISCARD: ' + lastKey)
        if key and item:
            self.__Order.append(key)
            self.cache_data[key] = item

    def get(self, key: str) -> Union[str, None]:
        '''Get value of key from cache dict'''
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
