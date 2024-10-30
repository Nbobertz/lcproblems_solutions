#here we are going to be given an array nums and an integer k. We are to return true if there are two distinct indices in the array such that nums[i] == nums[j] and that abs(i-j)<=k

#The simple explination here is that you want to see if there are two integers that are similar (1 and 1) and that the distance between these two points is <=k

#for this the easiest way to go about this is going to simply be loopingg through the array via two pointer. If we find two of the same element we then count to see if the trick falls into K. Now this could be an O(N) since we would have to at worst loop through the entire array. However, we could make it more efficent by simply adding a hashmap.

nums = [1,2,3,1,2,3]
k = 2

#below is two pointer solution
def solution():
    for p1 in range(0,len(nums)):
        for p2 in range(p1+1,len(nums)):
            if nums[p1]==nums[p2]:
                if abs(p2-p1)<=k:
                    return True
    return False

#below is hash solution
def solution2():
    d = {}

    for i, n in enumerate(nums):
        if n in d and abs(i - d[n]) <= k:
            return True
        else:
            d[n] = i

    return False

print(solution2())