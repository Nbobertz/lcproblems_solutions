"""
This is for the longest palindromic substring


"""


class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        if len(s) == 1:
            return s

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]  # expand goes one too far on both sides

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome
            p1 = expand(i, i)
            # Even-length palindrome
            p2 = expand(i, i + 1)

            # Pick the longest found so far
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2

        return longest