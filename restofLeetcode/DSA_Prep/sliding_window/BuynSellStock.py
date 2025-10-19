"""
Leetcode Classic, buy and sell stock

"""

class Solution(object):
    def maxProfit(self, prices):
        #sliding window problem here. The idea is that we will iterate over the array and move the l pointer if we see a smalelr day.

        answer = 0

        if not prices or len(prices) == 1:
            return answer

        l,r = 0,1
        while r <= len(prices)-1:
            if prices[l] < prices[r]:
                answer = max(answer,(prices[r]-prices[l]))
                #move l pointer
                r+=1
            elif prices[l]>=prices[r]:
                l = r
                r+=1
        return answer