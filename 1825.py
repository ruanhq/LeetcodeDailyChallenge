#1825. Finding MK average:
#仔细想，
"""
You are given two integers, m and k, and a stream of integers. 
You are tasked to implement a data structure that calculates 
the MKAverage for the stream.

The MKAverage can be calculated using these steps:

If the number of the elements in the stream is less than
 m you should consider the MKAverage to be -1. 
Otherwise, copy the last m elements of the stream to a separate container.
Remove the smallest k elements and the 
largest k elements from the container.
Calculate the average value for the rest of 
the elements rounded down to the nearest integer.
Implement the MKAverage class:

MKAverage(int m, int k) Initializes the MKAverage 
object with an empty stream and the two integers m and k.
void addElement(int num) Inserts a new element num into the stream.
int calculateMKAverage() Calculates and returns 
the MKAverage for the current stream rounded down to the nearest integer.

"""

class MKAverage:
    def __init__(self, m, k):
        self.m = m 
        self.k = k 
        self.List = SortedList([0] * m)
        self.sumK = 0
        self.sumM_K = 0
        self.queues = deque([0] * m)

    def addElement(self, num):
    	m = self.m 
    	k = self.k 
    	q = self.q 
    	List = self.List 

    	#update the queue:
    	q.append(num)
    	oldElement = q.popleft()
    	#remove the old num:



#Design类题目:
"""
1. Linked list related
2. LFU/LRU etc...
705/706/1381/1825 etc...
本周重点突破design类题目!!
"""










