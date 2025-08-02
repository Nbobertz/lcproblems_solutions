#here we are going to be given a series of intervals and we have to be able to print out all the non-overlapping intervals
#ex intervals = [[1,3],[2,5],[4,5]] = [[1,5]] None overlap

#the trick here is to sort all first index points in the intervals so that those line up. It makes this entire problem extremly easy.


intervals = [[1,3],[2,5],[10,12],[22,23]]

def solution(intervals):
    merged = []
    intervals.sort(key=lambda x : x[0])

    prev = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= prev[1]:
            prev[1] = max(prev[1], interval[1])
        else:
            merged.append(prev)
            prev = interval

    merged.append(prev)

    return merged

sol = solution(intervals)
print(sol)