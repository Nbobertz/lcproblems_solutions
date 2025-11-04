"""
Did buy/sell stock again for the 100th time. Pretty easy problem


"""

class Solution(object):
    def maxProfit(self, prices):
        answer = 0
        #capture edge cases
        if not prices or len(prices) == 1:
            return answer

        #now we have prices at len > 2
        l,r = 0,1
        while r != len(prices):
            #if r > l
            if prices[r] > prices[l]:
                tmp = prices[r] - prices[l]
                answer = max(answer,tmp)
                r+=1
            elif prices[r] <= prices[l]:
                #move l pointer
                l = r
                r+=1
        return answer
