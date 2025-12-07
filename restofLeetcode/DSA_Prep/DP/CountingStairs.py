"""
Here we are going to do dp top down memoisation dp
"""

# first buil a cache

cache = [-1] * n


def dfs(i):
    if i >= n:
        # i times we can hit n
        return i == n

    if cache[i] != -1:
        # pull from memory
        return cache[i]

    # Return the total number of ways to hit top of stairs
    cache[i] = dfs(i + 1) + dfs(i + 2)

    return cache[i]


return dfs(0)