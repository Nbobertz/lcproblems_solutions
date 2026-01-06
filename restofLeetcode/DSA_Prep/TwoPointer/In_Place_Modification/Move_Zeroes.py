"""
This is all abaout moving zeroes around. It can be compliicated if you are not careful.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        if not nums:
            return nums

        swap = 0

        for i,n in enumerate(nums):
            if n != 0:
                tmp = nums[i]
                nums[i] = nums[swap]
                nums[swap] = tmp
                swap+=1