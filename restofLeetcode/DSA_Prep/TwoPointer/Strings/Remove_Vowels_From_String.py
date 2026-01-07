""""
This is the remove vowels from string problem

"""

class Solution:
    def removeVowels(self, s: str) -> str:
        vows = set('aeiouAEIOU')

        answer = ""
        if not s:
            return answer

        for i,c in enumerate(s):
            if c not in vows:
                answer+=c

        return answer