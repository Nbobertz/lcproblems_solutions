"""
Same thing as prior. Doing it again to make sure I get it
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # ok, so we keep track of the sum as we progress. First we create prefix sum map with 0 array, then we add
        # to a counter as we go through
        # at each iteration we check counter -k if its in the prefix map. if it is then we add all of the results to the res and inc the counter by 1

        cursum = 0
        ans = 0
        if not nums or k == None:
            return ans

        # build prefix map
        pre = {0: 1}
        for n in nums:
            cursum += n
            res = cursum - k
            if res in pre:
                ans += pre[res]

            if cursum in pre:
                pre[cursum] += 1
            elif cursum not in pre:
                pre[cursum] = 1

        return ans