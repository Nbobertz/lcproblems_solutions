"""
This is the tribonachi number
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        memo = [0] * (n+1)

        memo[0] = 0
        memo[1] = 1
        memo[2] = 1


        def dfs(i): #only put 3 or greater in here
            if i >n:
                return

            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
            dfs(i+1)

        dfs(3)
        print(memo)
        return memo[-1]