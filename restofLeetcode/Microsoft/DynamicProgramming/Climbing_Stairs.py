#here we are going to be given a staircase with n amount of steps. You can either climb this staircase in 1 or 2 intervals. You need to return how many diffrent ways you can climb the staircase.

n = 5

def solution():
    # bottom up dynamic programing

    #handles the edge case of if there is 1 or 2 steps in the problem
    if n <= 2:
        return n


    dp = [0] * (n + 1) #creates the array that will store values of reaching steps at that increment

    dp[1], dp[2] = 1, 2 #makes the first and second array point manually store the values of 1 and 2 to reach that point


    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(solution())