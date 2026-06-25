"""
Here we just want to reverse a string
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = s[::-1]
        for x in range(len(s)):
            s[x] = tmp[x]