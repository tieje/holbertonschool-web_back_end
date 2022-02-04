#!/usr/bin/python3
'''2. LIFO Caching'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''LIFO Caching'''

    def __init__(self):
        '''Add input Order to keep track of order'''
        super().__init__()
        self.__inputOrder = []

    def put(self, key: str, item: str) -> None:
        '''
        Assign cache key to value
        If max items is reached, the last item put in will be removed.
        '''
        if BaseCaching.checkArgsIsNone(key, item):
            return
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.__inputOrder:
            LastKey: str = self.__inputOrder.pop()
            del self.cache_data[LastKey]
            print('DISCARD: ' + LastKey)
        self.__inputOrder.append(key)
        self.cache_data[key] = item
