"""
The idea here is that we need to buy and sell stock on each day
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        if not prices:
            return profit

        l = 0
        while l <= len(prices)-1:
            if l+1 <=len(prices)-1 and prices[l+1] > prices[l]:
                profit += (prices[l+1]-prices[l])
                l+=1
            else:
                #no larger,
                l+=1
                continue
        return profit