#231. Power of 2:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Merge into the main category
        #if n == 1:
        #    return False
        if n == 0:
            return False
        #Remove all of the 2 in the factorization of number n:
        while n % 2 == 0:
            n = n // 2
        if n == 1:
            return True
        else:
            return False
            
#342. Power of 4:
class Solution:
    def isPowerOfFour(self, n: int):
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1