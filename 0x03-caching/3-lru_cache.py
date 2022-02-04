#!/usr/bin/python3
'''3. LRU Caching'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''LRU Caching'''

    def __init__(self):
        '''Add input Order to keep track of order'''
        super().__init__()
        self.__inputOrder = []

    def put(self, key: str, item: str) -> None:
        '''
        Assign cache key to value
        If max items is reached, the most recently used item will be removed.
        '''
        if BaseCaching.checkArgsIsNone(key, item):
            return
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.__inputOrder:
            LastKey: str = self.__inputOrder.pop(0)
            del self.cache_data[LastKey]
            print('DISCARD: ' + LastKey)
        if key in self.__inputOrder:
            self.__inputOrder.remove(key)
        self.__inputOrder.append(key)
        self.cache_data[key] = item

    def get(self, key: str) -> str:
        '''Get value of key from cache dict'''
        if BaseCaching.checkArgsIsNone(key) or key not in self.cache_data:
            return 'None'
        self.__inputOrder.remove(key)
        self.__inputOrder.append(key)
        return self.cache_data[key]
