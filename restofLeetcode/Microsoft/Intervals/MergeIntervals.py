#here we are given a series of intervals in random order, it is our job to merge all the intervals and output a list of unique and non overappingg intervals

intervals = [[1,3],[2,6],[8,10],[15,18]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output