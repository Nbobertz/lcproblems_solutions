"""
Here we are taking hte longest string without repeating characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # this is a sliding window problem

        answer = 0
        if not s:
            return answer

        # o (n) space
        ss = set()

        l, r = 0, 1

        # o(1) time
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        elif len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2

        ss.add(s[l])

        # o(n) r pointer and l pointer iterate at most over n
        while r <= len(s) - 1:
            if s[r] not in ss:
                ss.add(s[r])
                r += 1
            answer = max(answer, r - l)
            while r <= len(s) - 1 and s[r] in ss:
                ss.remove(s[l])
                l += 1

        return answer
