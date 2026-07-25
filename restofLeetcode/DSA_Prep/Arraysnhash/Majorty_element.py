"""
Here we have an array and we want to return the majority element. The trick is to sort the array and return the middle point
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort and retrun the middle of hte array
        nums = sorted(nums)

        mid = len(nums) // 2
        return nums[mid]