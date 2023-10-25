#!/usr/bin/env python3
"""
   a class BasicCache that inherits from BaseCaching and is a caching system:
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
       a class BasicCache that inherits from BaseCaching
    """

    def put(self, key, item):
        """
           assigns to the dictionary self.cache_data
           the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
           returns the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
