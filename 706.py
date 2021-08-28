#706. design HashMap:
"""
Notes: defaultdict set a default value for an unexisting key here.
So using defaultdict will be slightly slower than the ordinary dict here.
"""
from collections import defaultdict 
class MyHashMap:
    def __init__(self):
        self.Maps = defaultdict(int)
    def put(self, key, value):
        if key in self.Maps:
            self.Maps[key] = value
        else:
            self.Maps[key] = value
    def get(self, key):
        if key in self.Maps:
            return self.Maps[key]
        else:
            return -1
    def remove(self, key):
        if key in self.Maps:
            del self.Maps[key]

####
#Ordinary list:
class MyHashMap:
    def __init__(self):
        self.Maps = {}
    def put(self, key, value):
        self.Maps[key] = value
    def get(self, key):
        if key in self.Maps.keys():
            return self.Maps[key]
        else:
            return -1
    def remove(self, key):
        if key in self.Maps.keys():
            del self.Maps[key]
