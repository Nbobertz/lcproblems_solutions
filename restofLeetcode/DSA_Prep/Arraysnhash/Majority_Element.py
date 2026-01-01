"""
This is to just find the majority element
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = None
        if not nums:
            return answer

        count = len(nums)//2

        if len(nums) == 1:
            return nums[0]

        hm = {}
        for i,n in enumerate(nums):
            if n not in hm:
                hm[n]=1
            elif n in hm:
                hm[n]+=1
                if hm[n] > count:
                    answer = n
                    return n