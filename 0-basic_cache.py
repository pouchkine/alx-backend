#!/usr/bin/python3
"""
frist caching implementations
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    return BasicCache
    """
    def put(self, key, item):
        if key == None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key == None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]




