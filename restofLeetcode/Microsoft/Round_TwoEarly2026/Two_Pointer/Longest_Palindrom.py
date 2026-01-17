"""
Here is the longest palindromic subsequence
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #I think expanding from the center is the way to go
        answer = ''
        if not s:
            return answer

        def expand(l,r):
            nonlocal answer
            while l >= 0 and r< len(s) and s[l] == s[r]:
                tmp = s[l:r+1]
                if len(tmp) >= len(answer):
                    answer = tmp
                l-=1
                r+=1
            return

        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        return answer