#here we are adding up the previous 3 numbers to get to the target n sequence in the fib sequence. 

class Solution:
    def tribonacci(self, n: int) -> int:

        # add the previous 3 values together to get the n value.

        # handles base case of nothing there or n is ==2 or below.
        if n <= 2:
            if n == 2:
                return 1
            else:
                return n

        # create memo and populate with our known increments.

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        # here we are simply just adding the value for n to the array at the n spot. Then we calc the next one by going back to the previous n value and adding that plus the other two

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]