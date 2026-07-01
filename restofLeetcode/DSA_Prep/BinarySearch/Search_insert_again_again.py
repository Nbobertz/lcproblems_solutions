"""
Here we are seeing how we can insert an integer in an input array using binary search. the idea is if it exists we can return thei ndex else return l
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