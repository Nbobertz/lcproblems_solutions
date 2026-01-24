"""
This is dynamic programming problem. We read from the array at each point


"""


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n

        def dfs(i):
            if i >= n:
                return i == n

            if memo[i] != -1:
                # already computed
                return memo[i]

            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]

        return dfs(0)