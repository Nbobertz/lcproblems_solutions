#the idea here is that we are given an array of intervals and the idea is that we need to loop through them and figure out how many intervals we can take out to make nothing overlapping.

intervals = [[1,2],[2,3],[3,4],[1,3]]

def solution():

    #first we sort the intervals so that we are always going to have the starting point
    intervals.sort()

    #const
    res = 0
    prevend = intervals[0][1]

    for start,end in intervals[1:]:
        if start >= prevend:
            prevend = end
        else:
            res +=1
            prevend = min(end,prevend)
    return res

print(solution())