#146. LRU Cache:
from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity
    def get(self, key: int):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
    #Utilize the OrderedDict here.
    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value 
        if len(self) > self.capacity:
            self.popitem(last = False)
    #Move the element to the end here.