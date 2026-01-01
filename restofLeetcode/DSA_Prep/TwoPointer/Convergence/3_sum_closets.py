"""
This is just 3 sum closest. It takes the closest we can get to the target\
"""

import math

if not nums or len(nums) < 3:
    return math.inf  # or some default value

nums = sorted(nums)
p1 = 0
closest_diff = math.inf
closest_sum = None  # this will store the actual sum

while p1 <= len(nums) - 3:
    l, r = p1 + 1, len(nums) - 1

    while l < r:
        ss = nums[p1] + nums[l] + nums[r]
        delta = abs(ss - target)

        # update closest sum if this is closer
        if delta < closest_diff:
            closest_diff = delta
            closest_sum = ss

        if ss < target:
            l += 1
        elif ss > target:
            r -= 1
        else:
            # exact match
            return ss

    p1 += 1

return closest_sum