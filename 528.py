#528. Random Pick with Weight:


class Solution:
    def __init__(self, w: List[int]):
        self.cumulativeSum = []
        cumSum = 0
        for weight in w:
            cumSum += weight
        accumSum = 0
        for weight in w:
            accumSum += weight/cumSum
            self.cumulativeSum.append(accumSum)

    def pickIndex(self):
        target = random.random()
        return bisect.bisect_left(self.cumulativeSum, target)
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        result = 0
        heap = []
        intervals.sort(key = lambda X: X[0])
        for interval in intervals:
        	#If there is no conflict, remove the smallest right interval point.
            while heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
            result = max(result, len(heap))
        return result


#######

def minMeeting










