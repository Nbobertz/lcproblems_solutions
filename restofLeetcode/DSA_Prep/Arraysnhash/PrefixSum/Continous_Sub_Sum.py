"""
This one is a tricky one where you have to understand hte complex logic.
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre = {0: -1}
        cursum = 0

        for i, n in enumerate(nums):
            cursum += n
            rem = cursum % k

            if rem in pre:
                if i - pre[rem] >= 2:
                    return True
            else:
                pre[rem] = i

        return False