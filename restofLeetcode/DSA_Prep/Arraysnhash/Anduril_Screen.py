"""
Here I was given an array of tuples and have to return the seen or previously seen
"""

zone_a = [('cat',1),('dog',2),('human',5),('Roger',10)]

def solution(zone,query):
    l,r = 0,len(zone)-1

    #query = 3

    while l<=r:
        half = (l+r)//2
        nn = zone[half][1]
        if nn<query:
            l = half+1
        elif nn >= query:
            r = half - 1
        elif nn == query:
            return zone[half][0]

    return zone[l-1][0]

print(solution(zone_a,12))
