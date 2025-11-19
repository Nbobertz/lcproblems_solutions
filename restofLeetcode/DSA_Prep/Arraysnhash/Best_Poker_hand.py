"""
Keep track of best poker hand via hashmaps
"""


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        # check for flush using set
        ss = set(suits)
        if len(ss) == 1:
            return 'Flush'

        hm = {}

        highest = 0

        for i, n in enumerate(ranks):
            highest = max(n, highest)
            if n not in hm:
                hm[n] = [1, i]
            elif n in hm:
                if hm[n][0] + 1 == 3:
                    return 'Three of a Kind'
                else:
                    hm[n][0] += 1

        for key, value in hm.items():
            if value[0] == 2:
                return 'Pair'
        return "High Card"
