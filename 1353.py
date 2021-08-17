#1353. maxiMum Number of events can be attended:
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]):
        events.sort()
        currentHeap = []
        eventId = 0
        maxTime = max(end for start, end in events)
        result = 0
        for day in range(1, maxTime + 1):
        	#use the while here
            while eventId < len(events) and events[eventId][0] == day:
                heappush(currentHeap, events[eventId][1])
                eventId += 1
            #remove the startPoint where has already passed.
            while currentHeap and currentHeap[0] < day:
                heappop(currentHeap)
            #
            if currentHeap:
                heappop(currentHeap)
                day += 1
                result += 1
        return result
