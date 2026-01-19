"""
This is binary search again
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this is just binary search
        if not nums:
            return nums

        l, r = 0, len(nums) - 1

        while l <= r:
            half = (l + r) // 2

            if nums[half] < target:
                l = half + 1
            elif nums[half] > target:
                r = half - 1

            elif nums[half] == target:
                return half

        return -1