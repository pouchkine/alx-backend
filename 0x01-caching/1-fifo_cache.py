#!/usr/bin/python3
"""
implementing FIFO cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    return BasicCache
    """
    def put(self, key, item):
        """
        put function
        """
        if key is None:
            pass
        else:
            #print(len(self.cache_data))
            if len(self.cache_data) == 0:
                self.listes = []
            self.cache_data[key] = item
            if len(self.cache_data) <=   FIFOCache.MAX_ITEMS:
                self.listes.append(key)
                self.cache_data[key] = item
            else:
                #print(len(self.cache_data))
                self.listes.append(key)
                self.listes.reverse()
                key_remove = self.listes.pop()
                print("DISCARD", key_remove)
                self.listes.reverse()
                self.cache_data.pop(key_remove)
                self.cache_data[key] = item
        #print(self.cache_data)

    def get(self, key):
        """
        get function
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
