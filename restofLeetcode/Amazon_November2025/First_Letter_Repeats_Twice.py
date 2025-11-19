"""
One of the easier ones. just repeat the character that repeats twice
"""

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # this can be handeled with a hashmap and lookup. Hashmap is o(1) time.

        hm = {}

        for char in s:
            if char not in hm:
                hm[char] = 1

            elif char in hm:
                return char
