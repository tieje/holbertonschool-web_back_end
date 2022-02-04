#!/usr/bin/python3
'''3. LRU Caching'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''MRU Caching'''

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
            FirstKey: str = self.__inputOrder[0]
            del self.cache_data[FirstKey]
            print('DISCARD: ' + FirstKey)
        if key in self.__inputOrder:
            self.__inputOrder.remove(key)
        self.__inputOrder.insert(0, key)
        self.cache_data[key] = item

    def get(self, key: str) -> str:
        '''Get value of key from cache dict'''
        if BaseCaching.checkArgsIsNone(key) or key not in self.cache_data:
            return 'None'
        self.__inputOrder.remove(key)
        self.__inputOrder.insert(0, key)
        return self.cache_data[key]
