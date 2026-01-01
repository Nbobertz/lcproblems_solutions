"""
This is a continuation of the previous problem. Got it first try but not optimal
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #[1,1,2,2,3,4,4] = [1,2,3,4]
        #1

        l = 0
        while l <= len(nums)-1:
            if l+1 <= len(nums)-1 and nums[l] == nums[l+1]:
                r = l+1
                while r <= len(nums)-1 and nums[l] == nums[r]:
                    nums.pop(l+1)
            l+=1
        print(nums)