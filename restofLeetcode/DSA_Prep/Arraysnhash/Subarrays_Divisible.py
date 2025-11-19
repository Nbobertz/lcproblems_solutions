"""
SUbarrays divisble by k
"""


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  # remainder 0 seen once (empty prefix)

        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            rem = prefix % k

            # previous same remainders produce valid subarrays
            ans += count[rem]

            count[rem] += 1

        return ans