"""
This is valid palindrome 2. It's jusst the first iterate
"""


class Solution:
    def makePalindrome(self, s: str) -> bool:

        answer = False
        if not s:
            return answer

        if len(s) == 1:
            return True

        l, r = 0, len(s) - 1

        count = 0
        while l <= r:
            if s[l] != s[r] and count < 2:
                count += 1
                l += 1
                r -= 1
                continue
            if s[l] != s[r] and count >= 2:
                # string splice to see if we have two similar strings
                s1 = s[:l] + s[l + 1:]  # takes out the one character we are at
                s2 = s[:r] + s[r + 1:]  # takes out the once character we are at
                return s1 == s1[::-1] or s2 == s2[::-1]
            l += 1
            r -= 1
        return True