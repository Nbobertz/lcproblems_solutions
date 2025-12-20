"""
Here we are going to calculate teh number of smooth descents in an array. This is just -1 from the previous day
"""


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        #this is a sliding window problem
        answer = 0

        ans,cnt = 1,1

        for i in range(1,len(prices)):
            if prices[i] == prices[i-1] -1:
                cnt+=1
            else:
                cnt = 1
            ans += cnt
        return ans