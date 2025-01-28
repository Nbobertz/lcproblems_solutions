#here we need to calculate a fibonachi number from a provided integer.
#the algorithm for fibinachi is f(n-1)+f(n-2) = n

n = 2

def solution(n):
    # do this with memoization

    memo = {0: 0, 1: 1}

    # now we need to recursivly call and add to the memo if we find something. We do this until we hit get larger then n then simply return the memo look up because it is o(1)

    def f(x):
        if x in memo:
            return memo[x]
        elif x not in memo:
            memo[x] = f(x - 1) + f(x - 2)
            return memo[x]

    return f(n)

answer = solution(n)

print(answer)