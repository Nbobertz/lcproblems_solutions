"""
Here we are checking if it is a subsequence
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0

        if s == '': return True
        if len(s) > len(t): return False

        while j < len(t):
            if s[i] == t[j]:
                if i == len(s) - 1:
                    return True
                i += 1

            j += 1
        return False