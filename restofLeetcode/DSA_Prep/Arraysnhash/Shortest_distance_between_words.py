"""
This is a two pointer pass at o(n2)

"""

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        #this is a sliding window problem

        if not wordsDict or not word1 or not word2:
            return None

        n = len(wordsDict)
        answer = n+1 #init to capture impossible

        for p1 in range(0,n):
            w1 = wordsDict[p1]
            if w1 == word1:
                for p2 in range(p1+1,n):
                    w2 = wordsDict[p2]
                    if w2 == word2:
                        answer = min(answer,abs(p1-p2))

            elif w1 == word2:
                for p2 in range(p1+1,n):
                    w2 = wordsDict[p2]
                    if w2 == word1:
                        answer = min(answer,abs(p1-p2))

        return answer