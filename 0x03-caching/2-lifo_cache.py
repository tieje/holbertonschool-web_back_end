#!/usr/bin/python3
'''2. LIFO Caching'''
from base_caching import BaseCaching
from typing import List, Union

class LIFOCache(BaseCaching):
    '''LIFO Caching'''

    def __init__(self):
        '''Add input Order to keep track of order'''
        super().__init__()
        self.__Order: List[str] = []

    def put(self, key: str, item: str) -> None:
        '''
        Assign cache key to value
        If max items is reached, the last item put in will be removed.
        '''
        if BaseCaching.checkArgsIsNone(key, item):
            return
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.__Order:
            LastKey: str = self.__Order.pop()
            del self.cache_data[LastKey]
            print('DISCARD: ' + LastKey)
        self.__Order.append(key)
        self.cache_data[key] = item

    def get(self, key: str) -> Union[str, None]:
        '''Get value of key from cache dict'''
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
