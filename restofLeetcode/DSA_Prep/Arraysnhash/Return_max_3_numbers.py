"""
You are given an array and you need to return the max of 3 numbers in the array. Trick is to sort it and then return the max of the last 3 or the max of the first 2 times the lats one
"""


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #why dont we sort and just * top 3?

        if len(nums) < 3:
            return 'non possible, need three numbers'

        nums = sorted(nums)
        ans1 = (nums[-1]*nums[-2])*nums[-3]
        ans2 = (nums[0]*nums[1])*nums[-1]
        return max(ans1,ans2)