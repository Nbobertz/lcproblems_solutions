"""
Did min cost of climbing stairs
"""

cache = [-1] * len(cost)


def dfs(i):
    if i >= len(cost):
        # zero to hit top
        return 0

    if cache[i] != -1:
        return cache[i]

    cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
    return cache[i]


return min(dfs(0), dfs(1))