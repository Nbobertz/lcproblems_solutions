"""
This is just the longest substring without a repeating character in it.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        l = 0
        answer = 0

        if not s:
            return answer

        for r in range(len(s)):

            while s[r] in ss:
                ss.remove(s[l])
                l += 1

            ss.add(s[r])
            answer = max(answer, r - l + 1)

        return answer
