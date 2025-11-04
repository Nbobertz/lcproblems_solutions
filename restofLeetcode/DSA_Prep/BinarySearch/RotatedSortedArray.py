"""
I got this problem done like 80% but could not finish up the logic on moving the pointers
"""

class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            half = (l + r) // 2

            # if mid element is greater than rightmost, min is to the right
            if nums[half] > nums[r]:
                l = half + 1
            else:
                r = half

        return nums[l]