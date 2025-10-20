#This is leetcodee 1128: number of equivilent dominoes pairs. Its an easy one but makes no sense in it's explination so I find it hard.

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        hm = {}
        answer = 0

        for a, b in dominoes:
            key = (min(a, b), max(a, b))

            if key in hm:
                answer += hm[key]
                hm[key] += 1

            else:
                hm[key] = 1
        return answer
