#!/usr/bin/python3
'''3. LRU Caching'''
from base_caching import BaseCaching
from typing import List, Union


class MRUCache(BaseCaching):
    '''MRU Caching'''

    def __init__(self):
        '''Add input Order to keep track of order'''
        super().__init__()
        self.__Order: List[str] = []

    def put(self, key: str, item: str) -> None:
        '''
        Assign cache key to value
        If max items is reached, the most recently used item will be removed.
        '''
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.__Order:
            FirstKey: str = self.__Order[0]
            del self.cache_data[FirstKey]
            print('DISCARD: ' + FirstKey)
        if key and item:
            if key in self.__Order:
                self.__Order.remove(key)
            self.__Order.insert(0, key)
            self.cache_data[key] = item

    def get(self, key: str) -> Union[str, None]:
        '''Get value of key from cache dict'''
        if not key or key not in self.cache_data:
            return None
        self.__Order.remove(key)
        self.__Order.insert(0, key)
        return self.cache_data[key]
