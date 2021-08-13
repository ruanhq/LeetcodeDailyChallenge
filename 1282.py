#1282. Group the People Given the Group Size They Belong to:

from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]):
        positionCounter = defaultdict(list)
        for i, size in enumerate(positionCounter):
            positionCounter[size].append(i)
        #Then iterate from scratch:
        result = []
        for s, l in positionCounter.items():
            for i in range(0, len(l), s):
                result.append(l[i: (i + s)])
        return result

