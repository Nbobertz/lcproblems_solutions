"""
Did house robber problem today. Was a doosy but next time I see it I will be able to get it
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        # i feel like this is literally counting stairs

        if not nums:
            return 0

        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(memo):
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]

        return dfs(0)