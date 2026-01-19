"""
THis is the relative ranks problem. I did it with a hashmap
"""

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = []
        if not score:
            return answer

        hm = {}
        for i,n in enumerate(score):
            hm[n] = i
        sor = sorted(score)[::-1]

        count = 1

        for s in sor:
            #s = 5
            hm[s] = count
            count+=1

        for i,s in enumerate(score):
            #capture 1=3
            if hm[s] == 1:
                score[i] = "Gold Medal"
            elif hm[s] == 2:
                score[i] = 'Silver Medal'
            elif hm[s] == 3:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(hm[s])
        return score