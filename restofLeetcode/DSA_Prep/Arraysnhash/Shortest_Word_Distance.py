"""
Find the shortest distance betwee nindex points for words
"""

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        answer = None

        if not wordsDict or not word1 or not word2:
            return answer

        hm = {}

        for i,n in enumerate(wordsDict):
            if n not in hm:
                hm[n] = [i]

            elif n in hm:
                hm[n].append(i)

        if len(hm[word1]) <= len(hm[word2]):
            for i1 in hm[word1]:
                for i2 in hm[word2]:
                    tmp = abs(i1-i2)
                    if answer!= None:
                        answer = min(tmp,answer)
                    elif answer == None:
                        answer = tmp

        elif len(hm[word2]) < len(hm[word1]):
            for i1 in hm[word2]:
                for i2 in hm[word1]:
                    tmp = abs(i1-i2)
                    if answer!= None:
                        answer = min(tmp,answer)
                    elif answer == None:
                        answer = tmp

        return answer
