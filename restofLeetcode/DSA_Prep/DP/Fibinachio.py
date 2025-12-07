"""
Did the fibonachi number sequence
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        # initialize cache with size n+1
        answer = [0] * (n + 1)
        answer[0] = 0
        answer[1] = 1

        def dfs(i):
            if i > n:
                return
            answer[i] = answer[i-1] + answer[i-2]
            dfs(i + 1)

        dfs(2)
        return answer[n]