#here we are going to be given an array and we need to count the number of bad pairs in it.

#You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

#Return the total number of bad pairs in nums.

nums = [4,1,3,3]

def solution():
    # bad pairs var
    badp = 0

    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if i < j and j - i != nums[j] - nums[i]:
                badp += 1

    return badp

print(solution())

