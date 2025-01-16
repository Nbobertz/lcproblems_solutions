#find out if a provided number is a power of two.
#return True if power and false if not
n = 16

def solution():
    num = 1
    if n == 1:
        return True
    while num<=n:
        tmp = num*2
        if tmp == n:
            return True
        num = tmp

def solution2():
    if n == 0:
        return False
    return n & (n - 1) == 0

#recursion
def isPowerOfTwo(self, n: int) -> bool:
    if n == 0: return False
    if n == 1: return True
    if n % 2 == 0:
        return isPowerOfTwo(n//2)
    else:
        return False

#print(solution())
print(isPowerOfTwo(n))