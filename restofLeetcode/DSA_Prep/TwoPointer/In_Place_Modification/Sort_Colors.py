"""
Here we want to sort colors in place. this is a classic problem that requires alot of typing out
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #don't return anything
        if not nums:
            return nums

        hm = {}

        #first pass, grab frequency map of everything
        for n in nums:
            if n not in hm:
                hm[n]=1
            elif n in hm:
                hm[n]+=1

        #second, pass replace number
        #[0,0,0,0]
        for i,n in enumerate(nums):
            if 0 in hm and n != 0:
                nums[i] = 0
                hm[0] -= 1
                if hm[0] == 0:
                    hm.pop(0)
            elif 0 in hm and n == 0:
                hm[0] -= 1
                if hm[0] == 0:
                    hm.pop(0)
            elif 1 in hm and n != 1:
                nums[i] = 1
                hm[1] -=1
                if hm[1] == 0:
                    hm.pop(1)
            elif 1 in hm and n == 1:
                hm[1] -= 1
                if hm[1] == 0:
                    hm.pop(1)
            elif 2 in hm and n != 2:
                nums[i] = 2
                hm[2] -= 1
                if hm[2] == 0:
                    hm.pop(2)
            elif 2 in hm and n == 2:
                hm[2] -= 1
                if hm[2] == 0:
                    hm.pop(2)