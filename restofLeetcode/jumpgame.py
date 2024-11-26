# DP or you can simply jump from first index


nums = [2,3,1,1,4]

def solution():
    l = 0
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False

    while l <= len(nums):
        if nums[l] == 0 and l != len(nums):
            return False
        if l == len(nums) - 1:
            return True
        l = nums[l] + l
    if l > len(nums):
        return True
    else:
        return False


def solution2():
    goal = len(nums)-1

    #loop backwards
    for i in range(len(nums) - 1, -1, -1):
        if i+nums[i]>=goal:
            goal = i
    if goal == 0:
        return True
    elif goal!=0:
        return False
print(solution2())