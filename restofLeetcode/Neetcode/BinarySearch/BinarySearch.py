"""
Flagship problem, we just half the result and move pniters. This only works because our input is sorted in some sore of order
"""

class Solution(object):
    def search(self, nums, target):

        #so this is just binary search

        l,r = 0,len(nums)-1

        while l<=r:
            half = (l+r)//2
            if nums[half]>target:
                r = half-1
            elif nums[half]<target:
                l = half + 1
            elif nums[half] == target:
                return half
        return -1