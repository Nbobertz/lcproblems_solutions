"""
Here we have a set mismatch where we need to find what number is doubled up and what number is missing betwene 1-n length of the array
"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        # create answer array
        ans = []

        # create a map
        hm = {}

        # go through and count
        for n in nums:
            if n not in hm:
                hm[n] = 1
            elif n in hm:
                ans.append(n)

        for x in range(len(nums) + 1):
            if x not in hm and x != 0:
                ans.append(x)

        return ans