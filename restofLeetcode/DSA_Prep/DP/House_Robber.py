"""
This is house robber, the trick here is to use a memo to keep track of each house robber point and see how large we can make the sum
"""

memo = {}


def dfs(i):
    if i >= len(nums):
        return 0

    if i in memo:
        return memo[i]

    memo[i] = max(
        nums[i] + dfs(i + 2),
        dfs(i + 1)
    )

    return memo[i]


return dfs(0)