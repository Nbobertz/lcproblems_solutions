"""
This one is removing duplicates from a sorted array that can appear at most 3 times
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #nums = [1,1,1,2,2,2,3,3,3,4,4,4] = [1,1,2,2,3,3,4,4]

        if len(nums) <= 2:
            return len(nums) #can't have it smaller

        k = 2 #starting from the third pos
        for i in range(2,len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k+=1
        return k

