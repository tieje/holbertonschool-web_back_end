#!/usr/bin/python3
'''0. Basic dictionary'''
from base_caching import BaseCaching
from typing import Union

class BasicCache(BaseCaching):
    '''Basic Cache'''

    def put(self, key: str, item: str) -> None:
        '''Add item to cache dict if key and item are defined'''
        if key and item:
            self.cache_data[key] = item

    def get(self, key: str) -> Union[str, None]:
        '''Get value of key from cache dict'''
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
