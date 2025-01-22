#so we are given an integer array nums, and we are to find the number of triplets that it will take to satisfy the constraints of i<j<k and that nums[i]+nums[j]+nums[k]%d == 0

nums = [3,3,4,7,8]

def bruteforce():
    if len(nums) < 3:
        return 0

        # keep track of count of triplets
    counter = 0

    for p1 in range(0, len(nums)):
        for p2 in range(p1 + 1, len(nums)):
            for p3 in range(p2 + 1, len(nums)):
                if p1 < p2 < p3 and (nums[p1] + nums[p2] + nums[p3]) % d == 0:
                    counter += 1
    return counter

def solution():
    