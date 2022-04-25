# https://leetcode.com/problems/lru-cache/submissions/

from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache: 
            return -1
        value = self.cache[key]
        #self.cache.move_to_end(key)
        del self.cache[key]
        self.cache.update({key: value})
        return value
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# param_1 = obj.get(1)
# obj.put(1,1)
