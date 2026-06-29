"""
Here we want to remove duplicates from a sorted array
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #two pointer in one o(n) pass

        if not nums:
            return []

        l = 0
        while l<= len(nums)-1:
            #check to see if +1 is in len of nums and the same
            while l+1 <= len(nums)-1 and nums[l] == nums[l+1]:
                nums.pop(l+1)

            l+=1
        return len(nums)