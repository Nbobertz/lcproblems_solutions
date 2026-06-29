"""
Here we want to do max contigous array problem. The idea is that we just need to keep track of ones and zeros and the index they are at if they match
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        zero, one = 0, 0
        res = 0

        index = {}  # stores counts

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            if one - zero not in index:
                index[one - zero] = i  # map to i so we can calc later

            if one == zero:
                res = one + zero
            else:
                idx = index[one - zero]
                res = max(res, (i - idx))

        return res