#!/usr/bin/python3
'''3. LRU Caching'''
from typing import List, Union
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''LRU Caching'''

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
            LastKey: str = self.__Order.pop(0)
            del self.cache_data[LastKey]
            print('DISCARD: ' + LastKey)
        if key and item:
            if key in self.__Order:
                self.__Order.remove(key)
            self.__Order.append(key)
            self.cache_data[key] = item

    def get(self, key: str) -> Union[str, None]:
        '''Get value of key from cache dict'''
        if not key or key not in self.cache_data:
            return None
        self.__Order.remove(key)
        self.__Order.append(key)
        return self.cache_data[key]
