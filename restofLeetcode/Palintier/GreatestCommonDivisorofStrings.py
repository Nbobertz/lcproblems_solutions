#here we are going to find the greatest common divisor of two strings provided. A subset can be a divisor.

def solution():
    if str1 + str2 != str2 + str1:
        return ""

    # Get the GCD of the two lengths.
    max_length = gcd(len(str1), len(str2))
    return str1[:max_length]