#381. Insert Delete GetRandom O(1) - Duplicates allowed
"""
Implement the RandomizedCollection class:

RandomizedCollection() Initializes the RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item was present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements (it's guaranteed that at least one element exists when this method is called). The probability of each element being returned is linearly related to the number of same values the multiset contains.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""
from random import choice
from collections import defaultdict
class RandomizedCollection:
    def __init__(self):
        self.list = []
        #using a dictionary to store the set of index corresponding to a value here
        self.index = defaultdict(set)
    def insert(self, val):
    	self.list.append(val)
        self.index[val].add(len(self.list) - 1)
        return len(self.index[val]) == 1
    #remove, 
    def remove(self, val):
        if not self.index[val]:
            return False
        #
        removeSampleIndex = self.index[val].pop()
        lastValue = self.list[-1]
        #exchange to the end of the list:
        self.list[removeSampleIndex] = lastValue
        #rotate the index of the lastValue 
        self.index[lastValue].add(removeSampleIndex)
        self.index[lastValue].discard(len(self.list) - 1)
        self.list.pop()
        return True
    #randomly choose a value from a list:
    def getRandom(self):
        return random.choice(self.list)

