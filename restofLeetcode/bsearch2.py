#standard binary search algo. THe idea here is to show how binary works

nums = [-1,0,2,4,6,8]
target = 10

def solution():
    l, r = 0, len(nums) - 1
    answer = -1
    while l <= r:
        halfpoint = int((l + r) / 2)
        if target < nums[halfpoint]:
            r = halfpoint - 1
        if target > nums[halfpoint]:
            l = halfpoint + 1
        if nums[halfpoint] == target:
            answer = halfpoint
            return answer
    return answer


print(solution())