"""
Pretty simplle, lc 1455 check if word is pre of word
"""

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')

        n = len(searchWord)

        for i,w in enumerate(words):
            if w[:n] == searchWord:
                return i+1

        return -1