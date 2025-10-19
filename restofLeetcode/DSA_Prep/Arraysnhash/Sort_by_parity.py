"""
Sort by parity is just find even's and insert at begining


"""

class Solution(object):
    def sortArrayByParity(self, nums):
        #let's do it in o(1) space and o(n) time

        #one pass, pop if even and insert
        for n in range(0,len(nums)):
            #find even
            if nums[n] % 2 == 0:
                tmp = nums.pop(n)
                nums.insert(0,tmp)
        return nums