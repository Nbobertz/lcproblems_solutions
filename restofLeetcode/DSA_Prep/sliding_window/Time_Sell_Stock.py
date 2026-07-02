"""
This is the best time to buy/sell stock problej
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #keep track of lowest, sell at highest

        import math

        maxp = 0
        lowest = math.inf
        for p in prices:
            if p <lowest:
                lowest = p
            elif p > lowest:
                maxp = max((p-lowest),maxp)

        return maxp