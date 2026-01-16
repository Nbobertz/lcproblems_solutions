#here we are given a series of intervals in an array and a new interval. Our goal here is to output an array of all new intervals including the one we were given.
#constraints are this: intervals can't overlap, intervals ending on the same number are coinsidered overlapping.

intervals = [[1,3],[6,9]]
newInterval = [2,5]

def solution(newInterval):
    # this is an intervals question; we simply need to loop through the array[arrays] and insert if it is needed

    # const answer array
    answer = []  # will store final product to return

    # one for loop through intervals [[1,4],[5,10],[20,30]] our interval is 9,22
    for i in range(0, len(intervals)):

        # capture the case of the interval comes before and return
        if newInterval[1] < intervals[i][0]:
            # append to answer, append the rest of intervals to answer, return
            answer.append(newInterval)
            return answer + intervals[i:]  # this pythonic way will return all intervals past i

        # capture case that our interval is greater then the current i intervals
        elif newInterval[0] > intervals[i][1]:
            # append our current intervals[i] to answer
            answer.append(intervals[i])  # we continue on since our newINterval is greater than the current i intervals

        else:  # now we have found an interval that overlaps. Build newInterval aggain using min,and max from both intervals[i] and newInterval
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

    # append new interval to array. This only works because our for loop would have appended it and returned by now had it not gotten to this. As such we can append it now and call it a day.
    answer.append(newInterval)

    return answer

print(solution(newInterval))