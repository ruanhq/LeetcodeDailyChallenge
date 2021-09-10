class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        n_meeting = len(intervals)
        for i in range(n_meeting - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
