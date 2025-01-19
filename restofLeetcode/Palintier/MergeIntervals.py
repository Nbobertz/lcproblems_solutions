#we are given an array of subarrays that represent intervals/ranges and our goal here is to go ahead and sort all overlaps

intervals = [[1,3],[2,6],[8,10],[15,18]]

def solution():
    # so we are given an array of range integers, the idea is that we have to remove all overlapping ranges and return only 'true' ranges. This an be done with a lambda function on sort and then just list comprehension

    # runs in o(nlogn) due to sort

    # sort the input intervals list
    intervals.sort(key=lambda i: i[0])
    answer = [intervals[0]]

    # why we sort
    # what if we have an input of [[1,4],[0,4]]? We would have a fail.

    # for loop to go through the aray
    for start, end in intervals[1:]:

        # what did we last end at at our first subarray in ranges?
        lastend = answer[-1][1]

        # if we overlap
        if start <= lastend:
            answer[-1][1] = max(lastend, end)

        # no overlap
        else:
            answer.append([start, end])
    return answer

print(solution())