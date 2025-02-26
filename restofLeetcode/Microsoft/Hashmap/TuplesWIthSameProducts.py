#here are are given a series of integers in a string and the idea is that we need to return the total amount of unique tuples we can return that satisfy the following
#the tuples need to be int1*int2 == int3*int4 and the numberes cant be the same
import collections
nums = [2,3,4,6,7,8]

def solution():
    ans = 0
    count = collections.Counter()

    for i in range(len(nums)):
        for j in range(i):
            prod = nums[i] * nums[j]
            ans += count[prod] * 8
            count[prod] += 1

    return ans

print(solution())