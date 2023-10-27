#!/usr/bin/env python3
"""
   a class LFUCache that inherits from BaseCaching and is a caching system
"""
from typing import Any, Optional
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
       class LFUCache inherits from Base Caching
    """
    def __init__(self):
        """
           initializes a new instance
        """
        super().__init__()
        self.counter = {}

    def put(self, key: Any, item: Any) -> None:
        """
           assigns to the dictionary self.cache_data
           the item value for the Key key
        """
        if not key or not item:
            return
        counter = self.counter
        new_cache_data = {key: item}
        old_cache_data = self.cache_data.get(key)
        if len(self.cache_data) == self.MAX_ITEMS and not old_cache_data:
            key_to_remove = list(counter.keys())[0]
            self.cache_data.pop(key_to_remove)
            counter.pop(key_to_remove)
            print(f'DISCARD: {key_to_remove}')
        self.cache_data.update(new_cache_data)
        counter.update({key: counter.get(key, 0) + 1})
        counter = dict(sorted(counter.items(),
                       key=lambda x: (x[1], x[0])))

    def get(self, key: Any) -> Optional[Any]:
        """
           return the value in self.cache_data linked to key
        """
        cache_item = self.cache_data.get(key)
        counter = self.counter
        if cache_item:
            counter.update({key: counter.get(key) + 1})
        counter = dict(sorted(counter.items(),
                       key=lambda x: (x[1], x[0])))
        return cache_item
