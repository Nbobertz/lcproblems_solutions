"""
Simple valid anagram problem
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #i think we can sort these
        ss,tt = list(s),list(t)
        ss.sort()
        tt.sort()

        if ss == tt:
            return True
        return False