"""
Got this first try via just sorting and returning
"""


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        nums2 = sorted(score)

        hm = {}

        for i, x in enumerate(nums2[::-1]):
            hm[x] = i

        answer = [0] * len(score)
        for i, p in enumerate(score):
            tmp = hm[p]
            if tmp == 0:
                answer[i] = 'Gold Medal'
            elif tmp == 1:
                answer[i] = 'Silver Medal'
            elif tmp == 2:
                answer[i] = 'Bronze Medal'
            else:
                answer[i] = str(hm[p] + 1)
        return answer

