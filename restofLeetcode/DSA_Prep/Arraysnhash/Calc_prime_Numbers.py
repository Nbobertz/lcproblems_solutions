"""
here we are given a n variable and need to calculate all prime numbers up to that n
"""
def solution():
    count = 0

    tmp = [True] * n

    if n > 0:
        tmp[0] = False
    if n > 1:
        tmp[1] = False

    for x in range(2, n):
        if tmp[x] == True:
            for x2 in range(x * x, n, x):
                tmp[x2] = False

    for x in range(n):
        if tmp[x] == True:
            count += 1

    return count