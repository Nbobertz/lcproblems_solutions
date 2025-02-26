#this is the second attempt at climbing stairs problem. Here you are given an n integer representing the height of a staircase.
#you can climb this staircase in either 1 or 2 step intervals. Your job is to return the total amount of steps it takes to climb the staircase

n = 5

#answer should be 8 for 5

def solution():
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]

    answer = dp[n]
    return answer


print(solution())