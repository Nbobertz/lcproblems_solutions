"""
Here we want to reverse words in a string and not have empty spaces outside of in between words
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ''
        if not s:
            return answer

        # splits on spaces, we then add them back
        words = s.split(' ')
        words = words[::-1]

        for w in words:
            if w != '':
                answer += w
                answer += ' '

        answer = answer[:-1]
        return answer

