#!/usr/bin/env python3
"""
   class FIFOCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
       class MRUCache that inherits from BaseCaching
    """

    def __init__(self):
        """
           initializes init function
        """
        super().__init__()
        self.mru_order = OrderedDict()

    def put(self, key, item):
        """
           to the dictionary self.cache_data the item value for the key key
           If key or item is None, this method should not do anything
        """
        if not key or not item:
            return

        self.mru_order[key] = item
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.mru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.mru_order) > BaseCaching.MAX_ITEMS:
            self.mru_order.popitem(last=False)
        self.mru_order.move_to_end(key, False)

    def get(self, key):
        """
           returns the value in self.cache_data linked to key
           If key is None or if the key doesn’t exist in
           self.cache_data, return None
        """
        if key in self.cache_data:
            self.mru_order.move_to_end(key, False)
            return self.cache_data[key]
        return None
