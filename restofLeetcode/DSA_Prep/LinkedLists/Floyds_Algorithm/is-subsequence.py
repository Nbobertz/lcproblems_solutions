"""
Here we are word is a subsequence of another word. It is a classic two pointer problem
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #create frequency map
        if not s:
            return True

        l = 0

        for char in t:
            if l <= len(s)-1 and char == s[l]:
                l+=1
        if l >= len(s):
            return True

        return False