"""
Classic substirng problem, two pointer solution, drag r pointer to endo f array and move l pointer ot compensate

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        ss = set()

        l = 0

        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l += 1

            ss.add(s[r])
            answer = max(answer, r - l + 1)

        return answer