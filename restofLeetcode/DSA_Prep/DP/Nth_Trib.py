"""
Here is the nth tribonachi number program

"""


class Solution:
    def tribonacci(self, n: int) -> int:
        # this is a dp problem
        if not n:
            return 0

        memo = [-1] * (n + 1)
        # we do the +1 because we need to acount that the first 3 of fib are literally just 0,1,1,

        if n == 4:
            return 4
        if n == 3:
            return 2
        if n == 2:
            return 1
        if n == 1:
            return 1
        if n == 0:
            return 0

        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        def dfs(i):
            # handle base case
            if i >= len(memo):
                return

            if memo[i] != -1:
                return memo[i]

            memo[i] = (memo[i - 1] + memo[i - 2] + memo[i - 3])
            dfs(i + 1)
            return memo[i]

        dfs(3)
        print(memo)
        return memo[n]