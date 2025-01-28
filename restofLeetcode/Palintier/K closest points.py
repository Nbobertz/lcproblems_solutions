#pretty simple problem. Given a graph your job is to simply iterate through all points and find the clsosest k ones to hte center. K is given to you along with the array of points.
points = [[1,3],[-2,2]]
k = 1

def solution():
    # here this is a heap problem. You need to understand how to get distance from current point but other then that it's just heaping together an array and poppping k times

    # create heap array
    heaparr = []

    # loop thorugh points, capture x and y, square it and heapify
    for x, y in points:
        dist = (x ** 2) + (y ** 2)
        heaparr.append([dist, x, y])

    # create heap
    heapq.heapify(heaparr)

    # create result array
    res = []
    while k:
        dist, x, y = heapq.heappop(heaparr)
        res.append([x, y])
        k -= 1

    return res


print(solution())