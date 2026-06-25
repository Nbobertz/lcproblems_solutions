"""
This is the first palindrom that we see
"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        answer = ''
        if not words:
            return answer

        for w in words:
            if w == w[::-1]:
                answer = w
                return answer

        return answer