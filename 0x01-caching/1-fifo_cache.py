#!/usr/bin/env python3
"""
   class FIFOCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
       class FIFOCache that inherits from BaseCaching
    """

    def __init__(self):
        """
           initializes init function
        """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
           to the dictionary self.cache_data the item value for the key key
           If key or item is None, this method should not do anything
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
           returns the value in self.cache_data linked to key
           If key is None or if the key doesn’t exist in
           self.cache_data, return None
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
