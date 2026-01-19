"""
This is about inserting an interval into a series of intervals
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1,3],[4,6]], [2,5] -> [1,6]
        # --2-3, 4---6
        # -1-------5

        answer = []
        n = len(intervals)
        i = 0

        # append first interval
        while i < n and intervals[i][1] < newInterval[0]:
            answer.append(intervals[i])
            i += 1

        while i <= n - 1 and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        answer.append(newInterval)

        while i < n:
            answer.append(intervals[i])
            i += 1

        return answer

