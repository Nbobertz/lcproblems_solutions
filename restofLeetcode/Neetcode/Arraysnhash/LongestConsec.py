"""
Here we have a long array of integers. We need to see waht teh longest consecutive seqence of integeres is

"""


class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        ss = set(nums)
        longest = 1

        for n in nums:
            # o(n)
            cnt = 1
            if n - 1 not in ss:
                x = n
                while x + 1 in ss:
                    cnt += 1
                    x += 1
            longest = max(longest, cnt)
        return longest