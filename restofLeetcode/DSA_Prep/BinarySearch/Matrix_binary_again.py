"""
Make sure to flatten array and then binary searhc over it
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary till failure, then insert at l since its in ascending order

        #we can edit this
        if not nums or target == None:
            return 'Nothing given'

        l,r = 0,len(nums)-1

        while l<=r:
            half = (l+r)//2

            if nums[half] < target:
                l = half+1
            elif nums[half] > target:
                r = half -1

            elif nums[half] == target:
                return half

        #at this point target is not in the array and we are at the same point. Just insert at l-1
        return l