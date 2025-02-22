#here we are given an array of integers in ascening order. The idea is that there are two of every integer except one and we need to return that one integer.

#While you can do this with one pass with a hashmap the condition is that your program has to run in o(logn) time.

nums = [1,1,2,3,3,4,4,8,8]

def hash_map_solution():
    # first pass is hashmap, at the end we return the element that appears only once.
    hm = {}

    for n in nums:
        if n not in hm:
            hm[n] = 1
        elif n in hm:
            hm[n] += 1

    # now loop through all points in dictionary
    for key, value in hm.items():
        if value == 1:
            return key

def binary_search_solution():
    #the idea here is that since we have an ascending order list of pairs of integers except one the len of hte list will always be odd. From here we can take the mid point, check left, check right then take the odd again until we don't have any more.