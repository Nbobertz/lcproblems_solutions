"""
This is about 3 sum going again
"""

answer = []
nums.sort()

for l in range(len(nums) - 2):
    if l > 0 and nums[l] == nums[l - 1]:
        continue

    if nums[l] > 0:
        break

    m, r = l + 1, len(nums) - 1
    while m < r:
        s = nums[l] + nums[m] + nums[r]

        if s < 0:
            m += 1
        elif s > 0:
            r -= 1
        else:
            answer.append([nums[l], nums[m], nums[r]])
            m += 1
            r -= 1

            while m < r and nums[m] == nums[m - 1]:
                m += 1
            while m < r and nums[r] == nums[r + 1]:
                r -= 1

return answer