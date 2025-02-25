#here we are given a series of meetings and asked to see if we can attend them all. This is an intervals question

intervals = [[0,30],[5,10],[15,20]]

def solution():
    intervals.sort()

    # grab the ending point of each interval and see if its in range of new interval
    answer = True

    # capture edge case of no intervals or 1 interval
    if len(intervals) == 0 or len(intervals) == 1:
        return answer

    counter = 0
    prevend = intervals[0][1]

    # loop through capturuing
    for start, end in intervals[1:]:
        if start < prevend:
            answer = False
            return answer
        else:
            prevend = end

    return answer

print(solution())