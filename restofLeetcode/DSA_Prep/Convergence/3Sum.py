"""
This is the classic 3 sum problem
"""

# step 1 read problem and ask clarying questions
# step 2 example input and output
# psudocode
# code up
# optimise and discuss

answer = []
if not nums or len(nums) < 3:
    return answer

nums = sorted(nums)
ss = set()

p1 = 0
while p1 <= len(nums) - 3:
    # now do two pointer
    l, r = p1 + 1, len(nums) - 1

    while l < r:
        # what if larger then 0
        if nums[p1] + nums[l] + nums[r] > 0:
            r -= 1
        elif nums[p1] + nums[l] + nums[r] < 0:
            l += 1
        elif nums[p1] + nums[l] + nums[r] == 0:
            # found a match
            if (nums[p1], nums[l], nums[r]) not in ss:
                answer.append([nums[p1], nums[l], nums[r]])
                ss.add((nums[p1], nums[l], nums[r]))
            l += 1
            r -= 1
    p1 += 1

return answer