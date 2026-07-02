"""
Longest string without repeating characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans = 1
        l, r = 0, 1
        ss = {s[0]}

        while r < len(s):
            if s[r] not in ss:
                ss.add(s[r])
                ans = max(ans, r - l + 1)
                r += 1
            else:
                while s[r] in ss:
                    ss.remove(s[l])
                    l += 1

        return ans