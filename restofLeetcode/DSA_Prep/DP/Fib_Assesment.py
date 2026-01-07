"""
This is the fib sequence with Dp


"""


class Solution:
    def fib(self, n: int) -> int:
        # this is a dp problem
        memo = [0] * (n + 1)

        if n == 0:
            return 0
        elif n == 1:
            return 1

        memo[0] = 0
        memo[1] = 1

        def fib(i):
            nonlocal memo
            if i >= n + 1:
                return

            # fib 4 = memo[3](1) + memo[2](1) = 3
            memo[i] = memo[i - 2] + memo[i - 1]
            fib(i + 1)
            return

        fib(2)
        print(memo)
        return memo[-1]