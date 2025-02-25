 #here we are given an array and asked the easeist way we could get to the end if at each point it cost ith points to move forward either 1 or two jumps.


cost = [1,2,3,4,5]

#this is a dynamic programmimng problem.

def solution():
    memo = [-1] * len(cost)  # builds the array to store the points at

    def dfs(i):
        if i >= len(cost):
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        return memo[i]

    return min(dfs(0), dfs(1))

print(solution())
