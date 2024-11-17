#here we are given an array with a random len with up to that len worth of nums inside it. We are guranteed to have at least one number repeat more then once. Goal here is to run in a linear time complexity.

#this is a set problem

nums = [3,1,3,4,2]

def solution():
    # this is a set problem. Simply iterate through array and return number if it's already in set

    # const set
    sset = set()

    # iterate through
    for p1 in range(0, len(nums)):
        if nums[p1] not in sset:
            sset.add(nums[p1])
        elif nums[p1] in sset:
            return nums[p1]

print(solution())