"""
This is the maximum repeating substirng problem
"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0

        if not word or not sequence:
            return count

        tmp = word

        while tmp in sequence:
            count += 1
            tmp+=word
        return count