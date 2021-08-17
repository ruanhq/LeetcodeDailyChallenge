#338. Counting Bits:
"""
1. remove the least signicant zero in the number:
x & (x - 1)
2. get the residual of value w.r.t 2:
x & 1
3. ans[x >> 1] + (x & 1)/ (x & 1)
ans[x] = ans[x >> 1] + (x & 1)
x & (x - 1) ----> Bit Manipulation

"""

class Solution:
    def countBits(self, num: int) -> List[int]:
    
        def countEachOne(x):
            count = 0
            while x != 0:
                x = x & (x - 1)
                count += 1
            return count
        result = [0] * (num + 1)
        for i in range(num + 1):
            result[i] = countEachOne(i)
        return result