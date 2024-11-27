class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxp = 0

        #go through array using sliding window.
        #after we take the profit at the current location.
        #if the right pointer is less then the left on we push lef to that location

        while r<=len(prices)-1:
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                maxp = max(profit,maxp)
            elif prices[l]>prices[r]:
                l=r
            r+=1
        return maxp