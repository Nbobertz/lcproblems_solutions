"""Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1."""


nums = [7,1,5,4]


def solution(nums):
    # we can do a two pointer pass through, it's going to be O(n2) since we are going to do two passes
    answer = None

    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            # logic for check
            if i < j and nums[i] < nums[j]:
                if answer == None:
                    answer = 0
                answer = max(answer, nums[j] - nums[i])

    if answer == None:
        return -1
    return answer

print(solution(nums))