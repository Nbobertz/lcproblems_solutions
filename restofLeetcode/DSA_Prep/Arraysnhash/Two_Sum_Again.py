"""
Two sum again. Simple stuff really

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #ok this is the classic one
        hm = {}

        for i,x in enumerate(nums):
            rem = target - x
            if rem in hm:
                return [hm[rem],i]
            hm[x] = i