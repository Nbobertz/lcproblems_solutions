"""
Best time to buy and sell stock here
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #this is a two pointer problem, the goal here is to move the left pointer if we see a lower number and calc the diff betwene the two largets
        maxp = 0 #max profit in this array
        if not prices or len(prices) == 1:
            return maxp

        l,r = 0,1

        while r <= len(prices)-1:
            #move left pointer
            if prices[r]<prices[l]:
                l=r
                r+=1
            elif prices[r]>=prices[l]:
                profit = prices[r]-prices[l]
                maxp = max(profit,maxp)
                r+=1
        return maxp