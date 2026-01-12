"""
Here we just want to see if the number is a palindrom number
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        return False
