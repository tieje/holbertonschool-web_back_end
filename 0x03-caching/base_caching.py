#!/usr/bin/python3
""" BaseCaching module
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key: str) -> str:
        '''Get value of key from cache dict'''
        if BaseCaching.checkArgsIsNone(key) or not self.cache_data.__contains__(key):
            return 'None'
        return self.cache_data[key]

    @ staticmethod
    def checkArgsIsNone(*args) -> bool:
        '''
        Check if args is None.
        If args is None return True.
        If args is not None return False.
        '''
        for i in args:
            if i is None:
                return True
        return False
