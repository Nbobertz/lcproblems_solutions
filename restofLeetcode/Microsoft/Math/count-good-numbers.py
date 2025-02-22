#here we are going to be given a series of integers and we have to see if they fit the constraints of a good number based off math.

# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).
#
# For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.
#
# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

def solution():
    MOD = 10 ** 9 + 7

    def expo(x: int, num: int) -> int:
        if num == 0:
            return 1
        elif num & 1 == 0:
            return expo(x ** 2 % MOD, num // 2)
        return x * expo(x, num - 1) % MOD

    return 5 ** (n % 2) * expo(20, n // 2) % MOD
