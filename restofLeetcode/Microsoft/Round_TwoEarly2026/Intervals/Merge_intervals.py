"""
Here we are going to merge the intervals. The trick is always that you need to sort based off hte firs index of the array
You can do this by arr1 = sorted(arr1,key=lambda pair: pair[0])
intervals = sorted(intervals,key = lambda pair:pair[0])
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        if not intervals:
            return answer

        #sort based off 0th index of interval
        intervals = sorted(intervals,key = lambda pair:pair[0])

        i = 0
        n = len(intervals) - 1
        #we inc index as we go along in while loop
        if not answer:
            answer.append(intervals[i])
            i+=1

        while i <= n:
            if answer[-1][1] < intervals[i][0]:
                answer.append(intervals[i])
                i+=1
            elif answer[-1][1] >= intervals[i][0]:
                while i <= n and answer[-1][1] >= intervals[i][0]:
                    answer[-1][0] = min(intervals[i][0],answer[-1][0])
                    answer[-1][1] = max(intervals[i][1],answer[-1][1])
                    i+=1

        return answer