"""
Here we are given an array and integer k. We need to return the total amount of all subarrays that can be multiplied up and be less then k
"""

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        prod = 1
        count = 0
        left = 0

        for right in range(len(nums)):
            prod *= nums[right]

            #shrink window if its greater then k
            while prod >= k:
                #remove nums[l] from prod and move l
                prod //= nums[left]
                left += 1
            count += right - left + 1
        return count