"""
This is just a lesson in string splicing
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        answer = False
        if not s:
            return answer

        if len(s) == 1:
            return True

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                s1 = s[:l] + s[l + 1:]
                s2 = s[:r] + s[r + 1:]
                return s1 == s1[::-1] or s2 == s2[::-1]
            l += 1
            r -= 1
        return True