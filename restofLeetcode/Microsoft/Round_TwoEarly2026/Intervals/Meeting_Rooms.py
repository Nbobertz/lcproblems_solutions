"""
Meeting rooms problem where we see if a person can attend all meetings
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # trick is to sort the intervals
        answer = True
        if not intervals:
            return answer

        intervals.sort(key=lambda meet: meet[0])

        i = 0
        n = len(intervals) - 1
        stack = []

        # go through and apply logic
        while i <= n:
            if not stack:
                stack.append(intervals[i])
                i += 1
            else:
                # now run logic on if false
                if stack[-1][1] > intervals[i][0]:
                    return False
                stack.append(intervals[i])
                i += 1
        return True