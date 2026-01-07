"""
This is literally just reversing vowels in a string
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [] #stores vowels
        index = [] #stores index points

        vows = set('aeiouAEIOU') #to compare against

        #one pass to capture all possible vowels
        for i,c in enumerate(s):
            if c in vows:
                index.append(i)
                vowels.append(c)

        s = list(s)
        vowels = vowels[::-1]

        for i,v in zip(index,vowels):
            s[i] = v

        res = "".join(s)
        return res